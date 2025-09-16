# Enhanced Synapse System: Advanced Intelligence Framework

A sophisticated, production-ready context engineering system implementing hybrid search, incremental updates, and vector embeddings for intelligent agent development.

## Overview

The Enhanced Synapse System combines Neo4j knowledge graphs, Redis caching, vector similarity search, and intelligent ingestion to provide agents with powerful, long-term memory and reasoning capabilities. Built following the Numogrammatic Codex principles for sustainable, scalable development.

## Key Enhancements

### Security Improvements
- Environment-based configuration with secure password generation
- Redis authentication with strong passwords
- Docker environment isolation
- Secure credential management

### Performance Optimizations
- Incremental ingestion with hash-based change detection
- Hybrid vector + graph search for improved relevance
- Enhanced caching with configurable TTL
- Optimized relationship creation

### Advanced Search Capabilities
- Vector embeddings for semantic similarity
- TF-IDF-based embeddings with upgrade path to transformers
- Multi-strategy search combining graph traversal and vector similarity
- Intelligent relevance scoring

### Operational Excellence
- Comprehensive error handling and logging
- Detailed ingestion statistics and progress tracking
- Health monitoring and staleness detection
- Automated cleanup of deleted files

## Architecture

```
~/.synapse-system/
├── neo4j/                     # Core system components
│   ├── .env                   # Secure environment configuration
│   ├── .venv/                 # Python virtual environment (uv-managed)
│   ├── activate.sh           # Master activation script (OODA Loop)
│   ├── docker-compose.yml    # Secured Neo4j & Redis services
│   ├── ingestion.py          # Enhanced ingestion engine
│   ├── context_manager.py    # Hybrid search API
│   ├── vector_engine.py      # Vector embedding system
│   ├── synapse_search.py     # Agent integration tool
│   └── vector_store.db       # SQLite vector database
├── instructions/             # Agent instruction files
├── standards/               # Coding and process standards
├── workflows/               # Automated workflows
└── templates/               # Reusable templates
```

## Core Technologies

- **Neo4j**: Graph database for relationship modeling
- **Redis**: High-performance caching with authentication
- **SQLite**: Vector storage with similarity search
- **Python**: Core implementation with uv package management
- **Docker**: Containerized services with secure configuration

## Quick Start Guide

### 1. System Activation
```bash
# Full activation with health checks and auto-ingestion
~/.synapse-system/neo4j/activate.sh

# Check system status
~/.synapse-system/neo4j/activate.sh --status

# Force complete re-ingestion
~/.synapse-system/neo4j/activate.sh --force

# Stop all services
~/.synapse-system/neo4j/activate.sh --stop
```

### 2. Manual Ingestion
```bash
cd ~/.synapse-system/neo4j
source .venv/bin/activate

# Incremental ingestion (default)
python ingestion.py

# Force full refresh
python ingestion.py --force

# View help
python ingestion.py --help
```

### 3. Context Search
```bash
cd ~/.synapse-system/neo4j
source .venv/bin/activate

# Search with automatic activation
python synapse_search.py "coding standards"

# Search with result limit
python synapse_search.py "implementation patterns" 3

# Check system health
python synapse_search.py --status

# JSON output
python synapse_search.py "query" --json
```

### 4. Vector Operations
```bash
cd ~/.synapse-system/neo4j
source .venv/bin/activate

# Generate test embedding
python vector_engine.py "sample text for embedding"

# View embedding statistics
python vector_engine.py --stats
```

## Configuration

### Environment Variables
The system uses `.env` file for configuration:

```bash
# Neo4j Configuration
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=<secure-generated-password>

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=<secure-generated-password>

# System Configuration
SYNAPSE_CACHE_TTL=3600
SYNAPSE_MAX_INGESTION_AGE=24

# Embedding Configuration
EMBEDDING_MODEL=simple_tfidf
EMBEDDING_DEVICE=cpu
EMBEDDING_BATCH_SIZE=16
```

### Service URLs
- **Neo4j Browser**: http://localhost:7474
- **Neo4j Bolt**: bolt://localhost:7687
- **Redis**: localhost:6379

## Core Features

### Incremental Ingestion
- Hash-based change detection for efficient updates
- Automatic cleanup of deleted files
- Detailed progress tracking and statistics
- Preserves existing data during updates

### Hybrid Search
- Vector similarity search for semantic matching
- Graph traversal for relationship discovery
- Combined relevance scoring
- Intelligent result ranking

### Vector Embeddings
- TF-IDF-based embeddings with normalized vectors
- 384-dimensional vectors (compatible with BGE-M3)
- Efficient similarity search with cosine distance
- Extensible framework for transformer models

### Graph Relationships
- Directory containment relationships
- File reference detection
- Type-based similarity grouping
- Smart relationship inference

### Caching and Performance
- Redis-based query result caching
- Configurable TTL for cache entries
- Connection pooling and optimization
- Batch processing for large operations

## API Integration

### Programmatic Access
```python
from synapse_search import search_synapse_context

# Basic search
result = search_synapse_context("implementation patterns")
context = result.get("context", {})

# Access structured results
primary_matches = context.get("primary_matches", [])
related_files = context.get("related_files", [])
key_concepts = context.get("key_concepts", [])

# Search with options
result = search_synapse_context(
    "coding standards",
    max_results=10,
    auto_activate=True
)
```

### Health Monitoring
```python
from context_manager import check_synapse_health, is_synapse_stale

# Check system health
health = check_synapse_health()
print(f"Status: {health['overall']['status']}")

# Check if data is stale
if is_synapse_stale():
    print("System needs re-ingestion")
```

## File Type Support

- **Markdown (.md)**: Documentation and instruction files
- **Python (.py)**: Implementation scripts and modules
- **Shell (.sh)**: Automation and deployment scripts
- **Text (.txt)**: General documentation and notes

## Troubleshooting

### Common Issues

**Services not starting**
```bash
# Check Docker daemon
sudo systemctl status docker

# Check port availability
netstat -tlnp | grep :7474
netstat -tlnp | grep :6379
```

**Connection failures**
```bash
# Verify environment configuration
cd ~/.synapse-system/neo4j
cat .env

# Test individual components
python context_manager.py --health
python vector_engine.py --stats
```

**Empty search results**
```bash
# Force re-ingestion
python ingestion.py --force

# Check file discovery
ls -la ~/.synapse-system/instructions/
ls -la ~/.synapse-system/standards/
```

**Permission errors**
```bash
# Fix script permissions
chmod +x ~/.synapse-system/neo4j/activate.sh

# Check directory permissions
ls -la ~/.synapse-system/
```

### Debug Commands
```bash
# System health check
python context_manager.py --health

# Ingestion statistics
python ingestion.py --help

# Vector embedding stats
python vector_engine.py --stats

# Service status
docker ps
docker logs neo4j_neo4j_1
docker logs neo4j_redis_1
```

## Development and Extension

### Adding New File Types
Modify `discover_files()` in `ingestion.py`:
```python
def discover_files(self) -> List[Path]:
    target_dirs = ["instructions", "standards", "workflows", "templates"]
    files = []

    for dir_name in target_dirs:
        dir_path = self.synapse_root / dir_name
        if dir_path.exists():
            files.extend(dir_path.rglob("*.md"))
            files.extend(dir_path.rglob("*.py"))
            files.extend(dir_path.rglob("*.sh"))
            files.extend(dir_path.rglob("*.txt"))
            files.extend(dir_path.rglob("*.yaml"))  # New type

    return files
```

### Upgrading to Transformer Embeddings
Replace the vector engine's `generate_embedding()` method:
```python
def transformer_embedding(self, text: str) -> np.ndarray:
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(self.embedding_model)
    embedding = model.encode(text, convert_to_numpy=True)
    return embedding / np.linalg.norm(embedding)  # Normalize
```

### Custom Relationship Types
Add new relationships in `create_relationships()`:
```python
# Create dependency relationships
session.run("""
    MATCH (a:SynapseFile), (b:SynapseFile)
    WHERE a.content CONTAINS ('import ' + b.name)
    MERGE (a)-[:DEPENDS_ON]->(b)
""")
```

## Performance Tuning

### Neo4j Optimization
- Increase heap size in `docker-compose.yml`
- Add appropriate indexes for frequent queries
- Enable query logging for analysis

### Redis Configuration
- Adjust memory allocation based on cache usage
- Configure eviction policies for cache management
- Monitor hit rates and adjust TTL values

### Vector Search Optimization
- Increase embedding dimensions for better accuracy
- Implement approximate nearest neighbor search for large datasets
- Batch vector operations for improved throughput

## Security Considerations

- All passwords are automatically generated and secured
- Redis requires authentication for all connections
- Docker containers run with minimal privileges
- Environment variables contain sensitive configuration
- No credentials are stored in code or logs

## Monitoring and Maintenance

### Regular Tasks
- Monitor disk usage for vector storage
- Check cache hit rates and memory usage
- Review ingestion logs for errors
- Verify service health and connectivity

### Backup Procedures
- Export Neo4j database regularly
- Backup vector storage SQLite database
- Save environment configuration securely
- Document custom configurations and extensions

## Philosophy and Design Principles

This system embodies the Numogrammatic Codex principle that complex systems require systematic mapping rather than avoidance. The hybrid approach acknowledges that different search strategies excel in different contexts, combining them intelligently rather than choosing one exclusively.

The Five Whys methodology is built into the error handling and diagnostic capabilities, encouraging deep analysis of system behavior rather than surface-level fixes.

The system is designed for evolution - starting with simple but effective implementations that can be upgraded to more sophisticated approaches as needs and resources grow.

---

**Enhanced Synapse System - Production-ready intelligence framework for agent development**