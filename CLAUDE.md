# CLAUDE.md

This file provides guidance to Claude Code when working with the Synapse System.

## Quick Start

```bash
# Start synapse services
~/.synapse-system/synapse start

# Initialize project with agents
cd your-project/
~/.synapse-system/synapse init .

# Search knowledge base
~/.synapse-system/synapse search "query terms"
```

## System Overview

Synapse System combines Neo4j knowledge graphs, Redis caching, and BGE-M3 vector embeddings to provide agents with persistent memory and semantic search capabilities.

## Essential Commands

### Synapse CLI
```bash
# Start/stop services
~/.synapse-system/synapse start
~/.synapse-system/synapse stop
~/.synapse-system/synapse status

# Search global knowledge
~/.synapse-system/synapse search "rust error handling"

# Initialize project with language-specific agents
~/.synapse-system/synapse init [directory]
```

### Legacy Commands
```bash
# Direct activation (advanced)
~/.synapse-system/.synapse/neo4j/activate.sh

# Manual ingestion
cd ~/.synapse-system/.synapse/neo4j && source .venv/bin/activate && python ingestion.py
```

## Project Integration

After running `synapse init`, projects get:
- `.claude/agents/language-specialist.md` (rust, typescript, golang, python)
- `.claude/agents/synapse-project-manager.md` (universal)
- `.synapse.yml` (project config)

### Using Agents
```bash
# In Claude Code:
@synapse-project-manager help with this project
@rust-specialist implement error handling
@typescript-specialist create a React component
```

## Architecture

### Core Components
- **.synapse/neo4j/**: Core system (ingestion, search, embeddings)
- **Neo4j**: Graph database (localhost:7474, bolt://localhost:7687)
- **Redis**: Cache (localhost:6379)
- **BGE-M3**: 1024-dimensional semantic vectors

### Data Flow
1. Ingestion: Process files into Neo4j knowledge graph
2. Embedding: BGE-M3 generates semantic vectors (SQLite storage)
3. Caching: Redis caches frequent queries
4. Retrieval: Hybrid search combines graph + vector similarity

## Dependencies

- Python 3.12+ with uv package manager
- Docker & Docker Compose
- BGE-M3 model (~2.3GB, auto-downloads)

## Key Principles

Follows the Numogrammatic Codex:
- **KISS**: Keep implementations simple
- **DRY**: Single source of truth
- **TDD**: Test-driven development
- **Five Whys**: Root cause analysis

For detailed setup instructions, see SETUP_GUIDE.md