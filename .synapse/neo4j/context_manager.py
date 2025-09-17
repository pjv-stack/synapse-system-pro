#!/usr/bin/env python3
"""
Synapse Context Manager
======================

The central API for intelligent context retrieval from the hybrid Neo4j/Redis system.
Implements the "Search then Traverse" pattern for optimal information synthesis.

Zone-0 Axiom: SoC (Separation of Concerns) - This class handles ONLY context retrieval,
not ingestion or activation.
"""

import os
import json
import sqlite3
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta

import redis
from neo4j import GraphDatabase
from dotenv import load_dotenv
from vector_engine import VectorEngine

load_dotenv()

class SynapseContextManager:
    """
    Central interface for intelligent context retrieval from the Synapse System.

    Implements hybrid search: Redis cache -> Graph traversal -> Synthesis
    """

    def __init__(self):
        self.synapse_root = Path.home() / ".synapse-system"
        self.neo4j_uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        self.neo4j_user = os.getenv("NEO4J_USER", "neo4j")
        self.neo4j_password = os.getenv("NEO4J_PASSWORD", "synapse_neo4j_pass")
        self.redis_host = os.getenv("REDIS_HOST", "localhost")
        self.redis_port = int(os.getenv("REDIS_PORT", 6379))
        self.redis_password = os.getenv("REDIS_PASSWORD", None)

        # Initialize connections
        self.driver = None
        self.redis_client = None
        self.sqlite_path = self.synapse_root / "neo4j" / "vector_store.db"
        self.vector_engine = VectorEngine(self.synapse_root)

        # Cache configuration
        self.cache_ttl = int(os.getenv("SYNAPSE_CACHE_TTL", 3600))  # 1 hour
        self.cache_prefix = "synapse:query:"

    def connect(self) -> bool:
        """Initialize connections to Neo4j and Redis"""
        try:
            self.driver = GraphDatabase.driver(
                self.neo4j_uri,
                auth=(self.neo4j_user, self.neo4j_password)
            )
            # Test connection
            with self.driver.session() as session:
                session.run("RETURN 1")

            self.redis_client = redis.Redis(
                host=self.redis_host,
                port=self.redis_port,
                password=self.redis_password,
                decode_responses=True
            )
            self.redis_client.ping()

            return True

        except Exception as e:
            print(f"Connection failed: {e}")
            return False

    def intelligent_search(self, user_query: str, max_results: int = 5) -> Dict[str, Any]:
        """
        The core "Search then Traverse" function.

        Returns a structured context summary optimized for agent consumption.
        """
        if not self.connect():
            return {"error": "Failed to connect to data stores"}

        # 1. Check Redis Cache First
        cache_key = f"{self.cache_prefix}{self._hash_query(user_query)}"
        cached_result = self.redis_client.get(cache_key)

        if cached_result:
            return {
                "source": "cache",
                "query": user_query,
                "context": json.loads(cached_result),
                "cached_at": "recently"
            }

        # 2. Perform Hybrid Search (Vector + Graph)
        relevant_nodes = self._hybrid_search(user_query, max_results)

        if not relevant_nodes:
            return {
                "source": "search",
                "query": user_query,
                "context": {"message": "No relevant files found in synapse system"},
                "nodes_found": 0
            }

        # 3. Enrich with Graph Traversal
        enriched_context = self._enrich_with_graph_data(relevant_nodes)

        # 4. Synthesize Final Context
        final_context = self._synthesize_context(enriched_context, user_query)

        # 5. Cache Result
        self.redis_client.setex(cache_key, self.cache_ttl, json.dumps(final_context))

        return {
            "source": "neo4j",
            "query": user_query,
            "context": final_context,
            "nodes_found": len(relevant_nodes),
            "cache_key": cache_key
        }

    def _hash_query(self, query: str) -> str:
        """Generate a hash for the query to use as cache key"""
        return hashlib.md5(query.lower().strip().encode()).hexdigest()

    def _hybrid_search(self, query: str, max_results: int) -> List[Dict]:
        """
        Hybrid search combining vector similarity and graph search.
        Returns nodes ranked by combined relevance score.
        """
        all_results = []

        # Vector search
        try:
            query_embedding = self.vector_engine.generate_embedding(query)
            vector_results = self.vector_engine.similarity_search(query_embedding, max_results * 2)

            # Get Neo4j nodes for vector matches
            if vector_results:
                node_ids = [result[0] for result in vector_results]
                vector_scores = {result[0]: result[1] for result in vector_results}

                with self.driver.session() as session:
                    # Batch fetch nodes by their IDs
                    placeholders = ", ".join(["$id" + str(i) for i in range(len(node_ids))])
                    params = {f"id{i}": node_id for i, node_id in enumerate(node_ids)}

                    result = session.run(f"""
                        MATCH (f:SynapseFile)
                        WHERE elementId(f) IN [{placeholders}]
                        RETURN f
                    """, **params)

                    for record in result:
                        node = dict(record["f"])
                        node_id = node_ids[0] if len(node_ids) == 1 else None  # Find correct ID
                        # Find the correct node ID by matching
                        for nid in node_ids:
                            # Try to get this node specifically to match
                            node_result = session.run("MATCH (f:SynapseFile) WHERE elementId(f) = $id RETURN f", id=nid)
                            node_record = node_result.single()
                            if node_record and dict(node_record["f"]) == node:
                                node_id = nid
                                break

                        if node_id:
                            node["relevance_score"] = vector_scores.get(node_id, 0.0)
                            node["match_type"] = "vector"
                            all_results.append(node)

        except Exception as e:
            print(f"Vector search failed: {e}")

        # Graph search as fallback/supplement
        graph_results = self._graph_search(query, max_results)

        # Combine results, avoiding duplicates
        existing_paths = {result.get("path") for result in all_results}
        for result in graph_results:
            if result.get("path") not in existing_paths:
                # Boost graph search scores slightly if no vector results
                boost = 0.1 if not all_results else 0.0
                result["relevance_score"] = result.get("relevance_score", 0) + boost
                result["match_type"] = "graph"
                all_results.append(result)

        # Sort by combined relevance score
        all_results.sort(key=lambda x: x.get("relevance_score", 0), reverse=True)

        return all_results[:max_results]

    def _graph_search(self, query: str, max_results: int) -> List[Dict]:
        """
        Search the Neo4j graph for relevant nodes.
        Uses full-text search on summaries and content.
        """
        # Prepare search terms
        search_terms = query.lower().split()

        with self.driver.session() as session:
            # Multi-strategy search
            results = []

            # Strategy 1: Summary contains any search terms
            summary_results = session.run("""
                MATCH (f:SynapseFile)
                WHERE ANY(term IN $terms WHERE toLower(f.summary) CONTAINS term)
                RETURN f,
                       size([term IN $terms WHERE toLower(f.summary) CONTAINS term]) as relevance_score
                ORDER BY relevance_score DESC
                LIMIT $limit
            """, terms=search_terms, limit=max_results)

            for record in summary_results:
                node = dict(record["f"])
                node["relevance_score"] = record["relevance_score"]
                node["match_type"] = "summary"
                results.append(node)

            # Strategy 2: File name or path contains terms (if we have space for more)
            if len(results) < max_results:
                name_results = session.run("""
                    MATCH (f:SynapseFile)
                    WHERE ANY(term IN $terms WHERE
                        toLower(f.name) CONTAINS term OR toLower(f.path) CONTAINS term)
                    AND NOT f.path IN $existing_paths
                    RETURN f,
                           size([term IN $terms WHERE
                               toLower(f.name) CONTAINS term OR toLower(f.path) CONTAINS term]) as relevance_score
                    ORDER BY relevance_score DESC
                    LIMIT $remaining
                """,
                terms=search_terms,
                existing_paths=[r["path"] for r in results],
                remaining=max_results - len(results))

                for record in name_results:
                    node = dict(record["f"])
                    node["relevance_score"] = record["relevance_score"]
                    node["match_type"] = "name"
                    results.append(node)

            return results

    def _enrich_with_graph_data(self, nodes: List[Dict]) -> List[Dict]:
        """
        Enrich the found nodes with their graph relationships.
        This implements the "Traversal" part of "Search then Traverse".
        """
        enriched_nodes = []

        with self.driver.session() as session:
            for node in nodes:
                node_path = node["path"]

                # Get relationships for this node
                relationships = session.run("""
                    MATCH (f:SynapseFile {path: $path})
                    OPTIONAL MATCH (f)-[r1:CONTAINS]->(child)
                    OPTIONAL MATCH (f)-[r2:REFERENCES]->(ref)
                    OPTIONAL MATCH (f)-[r3:SIMILAR_TO]->(similar)
                    OPTIONAL MATCH (parent)-[r4:CONTAINS]->(f)
                    RETURN
                        collect(DISTINCT {type: "contains", target: child.path, name: child.name}) as contains,
                        collect(DISTINCT {type: "references", target: ref.path, name: ref.name}) as references,
                        collect(DISTINCT {type: "similar_to", target: similar.path, name: similar.name}) as similar,
                        collect(DISTINCT {type: "contained_by", target: parent.path, name: parent.name}) as parents
                """, path=node_path)

                rel_data = relationships.single()

                enriched_node = node.copy()
                enriched_node["relationships"] = {
                    "contains": [r for r in rel_data["contains"] if r["target"] is not None],
                    "references": [r for r in rel_data["references"] if r["target"] is not None],
                    "similar_to": [r for r in rel_data["similar"] if r["target"] is not None],
                    "contained_by": [r for r in rel_data["parents"] if r["target"] is not None]
                }

                enriched_nodes.append(enriched_node)

        return enriched_nodes

    def _synthesize_context(self, enriched_nodes: List[Dict], query: str) -> Dict[str, Any]:
        """
        Synthesize the enriched graph data into a concise, token-efficient summary.
        This is the final "formatting" step optimized for agent consumption.
        """
        if not enriched_nodes:
            return {"summary": "No relevant content found"}

        # Group nodes by type and relevance
        high_relevance = [n for n in enriched_nodes if n.get("relevance_score", 0) >= 2]
        medium_relevance = [n for n in enriched_nodes if n.get("relevance_score", 0) == 1]

        synthesis = {
            "primary_matches": [],
            "secondary_matches": [],
            "related_files": [],
            "key_concepts": [],
            "suggested_actions": []
        }

        # Process high relevance matches
        for node in high_relevance:
            synthesis["primary_matches"].append({
                "file": node["name"],
                "path": node["path"],
                "summary": node["summary"],
                "type": node.get("type", "unknown"),
                "word_count": node.get("word_count", 0)
            })

        # Process medium relevance matches
        for node in medium_relevance:
            synthesis["secondary_matches"].append({
                "file": node["name"],
                "path": node["path"],
                "summary": node["summary"][:100] + "..." if len(node["summary"]) > 100 else node["summary"]
            })

        # Extract related files from relationships
        all_related = set()
        for node in enriched_nodes:
            rels = node.get("relationships", {})
            for rel_type in ["contains", "references", "similar_to", "contained_by"]:
                for rel in rels.get(rel_type, []):
                    if rel["target"]:
                        all_related.add((rel["target"], rel["name"]))

        synthesis["related_files"] = [
            {"path": path, "name": name}
            for path, name in list(all_related)[:5]  # Limit to 5 related files
        ]

        # Extract key concepts (simple keyword extraction)
        all_content = " ".join([node.get("summary", "") for node in enriched_nodes])
        words = all_content.lower().split()
        word_freq = {}
        for word in words:
            if len(word) > 3:  # Skip short words
                word_freq[word] = word_freq.get(word, 0) + 1

        synthesis["key_concepts"] = [
            word for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]
        ]

        # Generate suggested actions based on file types found
        file_types = set(node.get("type", "unknown") for node in enriched_nodes)
        if "md" in file_types:
            synthesis["suggested_actions"].append("Review documentation files for detailed instructions")
        if "sh" in file_types:
            synthesis["suggested_actions"].append("Check shell scripts for automation opportunities")
        if "py" in file_types:
            synthesis["suggested_actions"].append("Examine Python scripts for implementation patterns")

        return synthesis

    def check_health(self) -> Dict[str, Any]:
        """Check the health status of all system components"""
        health = {
            "neo4j": {"status": "unknown", "details": ""},
            "redis": {"status": "unknown", "details": ""},
            "files": {"status": "unknown", "count": 0},
            "overall": {"status": "unknown", "last_check": datetime.now().isoformat()}
        }

        # Check Neo4j
        try:
            if not self.driver:
                self.connect()

            with self.driver.session() as session:
                result = session.run("MATCH (f:SynapseFile) RETURN count(f) as file_count")
                file_count = result.single()["file_count"]

                health["neo4j"]["status"] = "healthy"
                health["neo4j"]["details"] = f"{file_count} files indexed"
                health["files"]["count"] = file_count
                health["files"]["status"] = "healthy" if file_count > 0 else "empty"

        except Exception as e:
            health["neo4j"]["status"] = "error"
            health["neo4j"]["details"] = str(e)

        # Check Redis
        try:
            if not self.redis_client:
                self.connect()

            self.redis_client.ping()
            cache_keys = len(self.redis_client.keys(f"{self.cache_prefix}*"))

            health["redis"]["status"] = "healthy"
            health["redis"]["details"] = f"{cache_keys} cached queries"

        except Exception as e:
            health["redis"]["status"] = "error"
            health["redis"]["details"] = str(e)

        # Overall status
        if (health["neo4j"]["status"] == "healthy" and
            health["redis"]["status"] == "healthy" and
            health["files"]["count"] > 0):
            health["overall"]["status"] = "healthy"
        elif health["files"]["count"] == 0:
            health["overall"]["status"] = "empty"
        else:
            health["overall"]["status"] = "degraded"

        return health

    def is_stale(self, max_age_hours: int = 24) -> bool:
        """
        Check if the synapse system data is stale and needs re-ingestion.
        Returns True if data is older than max_age_hours or doesn't exist.
        """
        try:
            if self.redis_client:
                metadata = self.redis_client.get("synapse:ingestion_metadata")
                if metadata:
                    meta_data = json.loads(metadata)
                    last_ingestion = datetime.fromisoformat(meta_data["last_ingestion"])
                    age = datetime.now() - last_ingestion
                    return age > timedelta(hours=max_age_hours)

            # Fallback: check Neo4j metadata
            if self.driver:
                with self.driver.session() as session:
                    result = session.run("""
                        MATCH (meta:SynapseMetadata {type: 'ingestion'})
                        RETURN meta.last_run as last_run
                        ORDER BY meta.last_run DESC
                        LIMIT 1
                    """)

                    record = result.single()
                    if record and record["last_run"]:
                        # Neo4j datetime comparison is complex, so we'll assume recent if exists
                        return False

            # If no metadata found, consider stale
            return True

        except Exception:
            # If any error occurs, consider stale
            return True

    def clear_cache(self) -> int:
        """Clear all cached query results. Returns number of keys deleted."""
        try:
            keys = self.redis_client.keys(f"{self.cache_prefix}*")
            if keys:
                return self.redis_client.delete(*keys)
            return 0
        except Exception:
            return 0

    def close(self):
        """Close all connections"""
        if self.driver:
            self.driver.close()
        if self.redis_client:
            self.redis_client.close()

# Convenience functions for external use
def search_synapse(query: str, max_results: int = 5) -> Dict[str, Any]:
    """Convenience function for one-off searches"""
    manager = SynapseContextManager()
    try:
        return manager.intelligent_search(query, max_results)
    finally:
        manager.close()

def check_synapse_health() -> Dict[str, Any]:
    """Convenience function for health checks"""
    manager = SynapseContextManager()
    try:
        return manager.check_health()
    finally:
        manager.close()

def is_synapse_stale() -> bool:
    """Convenience function for staleness checks"""
    manager = SynapseContextManager()
    try:
        return manager.is_stale()
    finally:
        manager.close()

if __name__ == "__main__":
    # Simple CLI interface for testing
    import sys

    if len(sys.argv) < 2:
        print("Usage: python context_manager.py <search_query>")
        print("       python context_manager.py --health")
        print("       python context_manager.py --stale")
        sys.exit(1)

    if sys.argv[1] == "--health":
        health = check_synapse_health()
        print(json.dumps(health, indent=2))
    elif sys.argv[1] == "--stale":
        stale = is_synapse_stale()
        print(f"System is {'stale' if stale else 'fresh'}")
    else:
        query = " ".join(sys.argv[1:])
        result = search_synapse(query)
        print(json.dumps(result, indent=2))