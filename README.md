# Synapse System: Hybrid Intelligence Framework

A sophisticated, automated context engineering system implementing the **Numogrammatic Codex** principles for agent-based development.

## Overview

The Synapse System combines Neo4j knowledge graphs, Redis caching, and intelligent ingestion to provide agents with powerful, long-term memory and reasoning capabilities. It implements the **OODA Loop** (Observe-Orient-Decide-Act) for self-healing and self-updating functionality.

## Architecture

```
~/.synapse-system/
├── neo4j/                     # Core system components
│   ├── activate.sh           # Master activation script (OODA Loop)
│   ├── docker-compose.yml    # Neo4j & Redis services
│   ├── ingestion.py          # Knowledge graph ingestion engine
│   ├── context_manager.py    # Hybrid search API
│   ├── synapse_search.py     # Agent integration tool
│   └── venv/                 # Python virtual environment
├── instructions/             # Agent instruction files
├── standards/               # Coding and process standards
├── workflows/               # Automated workflows
└── templates/               # Reusable templates
```

## Core Principles (Zone-0 Axioms)

- **KISS**: Keep It Simple, Stupid - Reduce complexity systematically
- **Feighnburm Constant (𝔽)**: Acknowledge emergent complexity, map it
- **DRY**: Don't Repeat Yourself - Single truth, single place
- **SoC**: Separation of Concerns - Clean partitioning
- **TDD**: Test-Driven Development guides implementation

## Quick Start

### 1. Activate the System
```bash
# Full activation with health checks and auto-ingestion
~/.synapse-system/neo4j/activate.sh

# Check status only
~/.synapse-system/neo4j/activate.sh --status

# Force re-ingestion
~/.synapse-system/neo4j/activate.sh --force
```

### 2. Search for Context
```bash
cd ~/.synapse-system/neo4j
source venv/bin/activate

# Search via Python API
python synapse_search.py "coding standards"
python synapse_search.py "how to execute tasks" 3

# Check system health
python synapse_search.py --status
```

### 3. Agent Integration
```python
# In your agent code
from synapse_search import search_synapse_context

result = search_synapse_context("implementation patterns")
context = result.get("context", {})

# Access structured results
primary_matches = context.get("primary_matches", [])
related_files = context.get("related_files", [])
```

## System Components

### 🧠 Ingestion Engine (`ingestion.py`)
- Discovers files in synapse directories
- Generates AI summaries (currently rule-based, extensible to LLM)
- Populates Neo4j knowledge graph
- Creates structural relationships
- Prepares vector metadata for future ML enhancement

### 🔍 Context Manager (`context_manager.py`)
- Implements "Search then Traverse" pattern
- Redis caching for performance
- Graph traversal for relationship discovery
- Intelligent context synthesis
- Health monitoring and staleness detection

### 🚀 Activation Workflow (`activate.sh`)
- OODA Loop implementation
- Docker service management
- Automatic health checks
- Smart re-ingestion logic
- Self-healing capabilities

### 🔌 Agent Tool (`synapse_search.py`)
- Simple agent integration interface
- Automatic system activation
- Formatted output for agent consumption
- CLI and programmatic access

## The OODA Loop in Action

The activation script implements the OODA cycle:

1. **Observe**: Check environment and service status
2. **Orient**: Analyze what needs to be done
3. **Decide**: Determine if re-ingestion is needed
4. **Act**: Perform necessary updates and ingestion

## Services Management

### Start Services
```bash
cd ~/.synapse-system/neo4j
docker-compose up -d
```

### Stop Services
```bash
~/.synapse-system/neo4j/activate.sh --stop
```

### Service URLs
- **Neo4j Browser**: http://localhost:7474
- **Neo4j Bolt**: bolt://localhost:7687
- **Redis**: localhost:6379

### Default Credentials
- **Neo4j**: neo4j / synapse_neo4j_pass
- **Redis**: No authentication (localhost only)

## File Types Supported

- **📄 Markdown (.md)**: Documentation, instructions
- **🔧 Shell Scripts (.sh)**: Automation scripts
- **🐍 Python (.py)**: Implementation code
- **📝 Text (.txt)**: General documentation

## Configuration

Copy `.env.example` to `.env` and customize:

```bash
cd ~/.synapse-system/neo4j
cp .env.example .env
# Edit .env with your preferences
```

## Future Enhancements

The system is designed for easy extension:

1. **Vector Embeddings**: SQLite schema ready for ML models
2. **AI Summaries**: API integration placeholder for LLM services
3. **Advanced Relationships**: Graph algorithms for deeper insights
4. **Real-time Updates**: File watching for automatic ingestion

## Troubleshooting

### Common Issues

1. **Services not starting**: Check Docker daemon
2. **Connection failures**: Verify service ports
3. **Empty results**: Run force re-ingestion
4. **Permission errors**: Check script permissions

### Debug Commands
```bash
# Check system health
python context_manager.py --health

# Test connections
python context_manager.py --stale

# Manual ingestion
python ingestion.py
```

## Philosophy

This system embodies the **Numogrammatic Codex** principle that in any sufficiently complex system, emergent properties will manifest. Instead of ignoring this complexity, we map it systematically, creating **zones** of understanding that enable intelligent navigation through the **currents** of information and relationships.

The **Five Whys** methodology is built into the design, encouraging deep root-cause analysis rather than surface-level solutions.

---

*"The Feighnburm Constant: Acknowledge emergent complexity, map it; never ignore it."*