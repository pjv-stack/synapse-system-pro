# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## System Overview

Synapse System is a hybrid intelligence framework combining Neo4j knowledge graphs, Redis caching, and BGE-M3 vector embeddings to provide agents with persistent memory and semantic search capabilities.

## Essential Commands

### System Activation & Management
```bash
# One-command system activation (starts services, checks health, runs ingestion)
~/.synapse-system/.synapse/neo4j/activate.sh

# Check system health status
~/.synapse-system/.synapse/neo4j/activate.sh --status

# Force re-ingestion of all files
~/.synapse-system/.synapse/neo4j/activate.sh --force

# Stop all services
~/.synapse-system/.synapse/neo4j/activate.sh --stop
```

### Development Commands
```bash
# Activate Python virtual environment
cd ~/.synapse-system/.synapse/neo4j
source .venv/bin/activate

# Run manual ingestion
python ingestion.py

# Search knowledge base
python synapse_search.py "query terms"

# Check service health programmatically
python context_manager.py --health
```

### Docker Services
```bash
# View service status
docker-compose ps

# View logs
docker-compose logs neo4j
docker-compose logs redis
```

## Architecture

### Core Components

- **.synapse/neo4j/activate.sh**: Master orchestration script implementing OODA Loop (Observe-Orient-Decide-Act)
- **.synapse/neo4j/ingestion.py**: Discovers and processes files into Neo4j knowledge graph
- **.synapse/neo4j/context_manager.py**: Hybrid search API combining graph traversal with vector similarity
- **.synapse/neo4j/vector_engine.py**: BGE-M3 embedding generation (1024-dimensional vectors)
- **.synapse/neo4j/synapse_search.py**: Simple interface for agent integration

### Data Flow

1. **Ingestion**: Files from .synapse/instructions/, .synapse/standards/, .synapse/templates/, .synapse/tools/ are processed
2. **Embedding**: BGE-M3 generates semantic vectors stored in SQLite
3. **Graph Storage**: Relationships stored in Neo4j with metadata
4. **Caching**: Redis caches frequent queries for performance
5. **Retrieval**: Hybrid search combines graph relationships with vector similarity

### Service Architecture

- **Neo4j**: Graph database on localhost:7474 (web) and bolt://localhost:7687
- **Redis**: Cache on localhost:6379
- **SQLite**: Local vector storage at .synapse/neo4j/vector_store.db

## Project Integration

### Setting Up Synapse for a Project
```bash
# Copy synapse to project
cp -r ~/.synapse-system/.synapse /path/to/project/.synapse

# Use synapse-project-manager agent in Claude Code
# It will auto-detect language and configure appropriately
```

### Project-Specific Search
```bash
cd project/.synapse/neo4j
source .venv/bin/activate
python synapse_search.py "project specific query"
```

## Key Implementation Principles

The system follows the Numogrammatic Codex:
- **KISS**: Keep implementations simple, reduce complexity
- **DRY**: Single source of truth for each instruction
- **SoC**: Clean separation between ingestion, storage, and retrieval
- **TDD**: Test-driven development approach
- **Five Whys**: Root cause analysis methodology

## Dependencies

- Python 3.12+ with uv package manager
- Docker & Docker Compose for services
- Python packages: neo4j, redis, sentence-transformers, sqlite-vss
- BGE-M3 model (~2.3GB, auto-downloads on first use)

## Environment Variables

Configuration in .synapse/neo4j/.env:
- NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD
- REDIS_HOST, REDIS_PORT, REDIS_PASSWORD
- EMBEDDING_MODEL=BAAI/bge-m3