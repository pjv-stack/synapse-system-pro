# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Quick Start

```bash
# Start synapse services
~/.synapse-system/synapse start

# Initialize your project with agents
cd your-project/
~/.synapse-system/synapse init .

# Use agents in Claude Code:
# @synapse-project-manager help with this project
# @rust-specialist implement async patterns
```

## System Overview

Synapse System is a hybrid intelligence framework combining Neo4j knowledge graphs, Redis caching, and BGE-M3 vector embeddings to provide agents with persistent memory and semantic search capabilities.

## Essential Commands

### Synapse CLI (Simplified)
```bash
# Start synapse services (Neo4j, Redis)
~/.synapse-system/synapse start

# Check system health
~/.synapse-system/synapse status

# Stop services
~/.synapse-system/synapse stop

# Search global knowledge base
~/.synapse-system/synapse search "query terms"

# Initialize project with language-specific agents
~/.synapse-system/synapse init [directory]

# Show help
~/.synapse-system/synapse help
```

### Legacy Commands (Still Available)
```bash
# Direct activation script (advanced users)
~/.synapse-system/.synapse/neo4j/activate.sh

# Manual ingestion
cd ~/.synapse-system/.synapse/neo4j && source .venv/bin/activate && python ingestion.py

# Direct Python access (advanced)
cd ~/.synapse-system/.synapse/neo4j && source .venv/bin/activate && python context_manager.py --health
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
# Initialize any project with language-specific agents
cd /path/to/project
~/.synapse-system/synapse init .

# This creates:
# - .claude/agents/language-specialist.md (rust, typescript, golang, python)
# - .claude/agents/synapse-project-manager.md (universal)
# - .synapse.yml (project config)
```

### Using Project Agents
```bash
# In Claude Code, use the agents:
@synapse-project-manager help with this project
@rust-specialist implement error handling
@typescript-specialist create a React component
```

### Global Knowledge Search
```bash
# Search from anywhere (uses global knowledge base)
~/.synapse-system/synapse search "project patterns rust"
~/.synapse-system/synapse search "testing strategies typescript"
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