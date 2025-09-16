# Synapse System: A Hybrid Intelligence Framework

Automated context engineering system for agent-based development with BGE-M3 semantic embeddings.

## Prerequisites

Before setting up Synapse, ensure you have:

- **Python 3.12+** - Modern Python with async support
- **uv package manager** - Fast Python package installer
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- **Docker & Docker Compose** - For Neo4j and Redis services
- **Git** - Version control

## Overview

The Synapse System combines Neo4j knowledge graphs, Redis caching, and BGE-M3 vector embeddings to provide agents with long-term memory and reasoning capabilities. It implements the **OODA Loop** (Observe-Orient-Decide-Act) for self-healing and self-updating functionality.

### Key Features

- **BGE-M3 Embeddings**: 1024-dimensional semantic vectors running locally (no API keys)
- **Hybrid Search**: Combines graph traversal with vector similarity
- **Language Detection**: Automatic project context understanding
- **Agent Integration**: Designed for Claude Code workflows
- **Knowledge Persistence**: Long-term memory across sessions

## Architecture

```
~/.synapse-system/                # Global installation
├── neo4j/                       # Core system components
│   ├── activate.sh             # Master activation script (One Command Setup)
│   ├── docker-compose.yml      # Neo4j & Redis services
│   ├── ingestion.py            # Knowledge graph ingestion engine
│   ├── context_manager.py      # Hybrid search API
│   ├── vector_engine.py        # BGE-M3 embedding system
│   ├── synapse_search.py       # Agent integration tool
│   └── .venv/                  # Python virtual environment
├── instructions/               # Agent instruction files
├── standards/                 # Coding and process standards
├── workflows/                 # Automated workflows
├── templates/                 # Reusable templates
└── tools/                     # Agent tools (synapse-project-manager.md)

project/                         # Your project directory
└── .synapse/                   # Project-specific synapse instance
    ├── context_manager.py      # Local search capabilities
    ├── vector_engine.py        # Local embeddings
    ├── config.json            # Project configuration
    └── instructions/          # Project-specific context
```

## Core Principles (Zone-0 Axioms)

- **KISS**: Keep It Simple, Stupid - Reduce complexity systematically
- **Feighnburm Constant (𝔽)**: Acknowledge emergent complexity, map it
- **DRY**: Don't Repeat Yourself - Single truth, single place
- **SoC**: Separation of Concerns - Clean partitioning
- **TDD**: Test-Driven Development guides implementation

## Quick Start

### 1. Global System Setup (One Command)
```bash
# Activate the entire synapse system
~/.synapse-system/neo4j/activate.sh

# Check system health
~/.synapse-system/neo4j/activate.sh --status

# Force re-ingestion
~/.synapse-system/neo4j/activate.sh --force
```

### 2. Project Setup (Manual Copy + Agent)

#### Step 1: Copy Synapse to Your Project
```bash
# Navigate to your project
cd /path/to/your/project

# Copy synapse system
cp -r ~/.synapse-system .synapse
```

#### Step 2: Use the Synapse Project Manager Agent

In Claude Code, invoke the `synapse-project-manager` agent:

```
@synapse-project-manager

Please set up synapse for this project. Detect the language, configure the appropriate templates and standards, and initialize the vector store.
```

The agent will:
- 🔍 **Auto-detect project language** (Rust, Go, TypeScript, etc.)
- ⚙️ **Configure synapse** for your project context
- 📚 **Set up language-specific templates** and standards
- 🧠 **Initialize BGE-M3 embeddings** for semantic search
- 🗃️ **Ingest project knowledge** into the vector store

### 3. Search for Context
```bash
cd ~/.synapse-system/neo4j
source .venv/bin/activate

# Search via Python API
python synapse_search.py "rust error handling patterns"

# Direct Python usage for global search
python context_manager.py
```

### 4. Project-Specific Search
```bash
# In your project with .synapse/ directory
cd project/.synapse
source .venv/bin/activate
python search.py "project specific query"
```

## BGE-M3 Embeddings

### What is BGE-M3?

BGE-M3 (Beijing Academy of Artificial Intelligence - Multilingual, Multifunctionality, Multimodality) provides:

- **1024-dimensional vectors** for rich semantic representation
- **100+ language support** for multilingual projects
- **Local execution** - no API keys or internet required after initial download
- **Automatic caching** at `~/.cache/huggingface/hub/`

### First-Time Setup

On first use, BGE-M3 downloads automatically (~2.3GB):
```
Loading BGE-M3 model: BAAI/bge-m3
BGE-M3 model loaded successfully.
```

### Configuration

In `.env` file:
```bash
# Use BGE-M3 (recommended)
EMBEDDING_MODEL=BAAI/bge-m3

# Or fallback to TF-IDF
EMBEDDING_MODEL=simple_tfidf
```

## Agent Integration

### Synapse Project Manager Agent

The system includes a specialized agent (`tools/synapse-project-manager.md`) for project setup:

**Capabilities:**
- 🔍 Auto-detect project language from files (Cargo.toml, package.json, go.mod, etc.)
- ⚙️ Configure language-specific templates and standards
- 🧠 Initialize BGE-M3 embeddings for the project
- 📚 Set up project-specific knowledge base
- 🗃️ Ingest project documentation and configuration

**Usage in Claude Code:**
```
@synapse-project-manager

I've copied synapse to my project. Please detect the language and set up the knowledge base.
```

### Claude Code Integration

Use synapse search in any agent:

```python
# Search for implementation patterns
context = synapse_search("error handling patterns rust")
# Returns relevant patterns from knowledge base
```

## OODA Loop Implementation

### Observe
- Monitor file system changes
- Track agent interaction patterns
- Collect performance metrics

### Orient
- Analyze knowledge graph relationships
- Identify knowledge gaps
- Assess system health

### Decide
- Determine ingestion priorities
- Select optimization strategies
- Plan knowledge expansion

### Act
- Execute incremental ingestion
- Update relationships
- Optimize search performance

## Advanced Usage

### Manual Ingestion
```bash
cd ~/.synapse-system/neo4j
source .venv/bin/activate
python ingestion.py --force  # Full refresh
```

### Custom Search Strategies
```bash
# Search global knowledge base
python synapse_search.py "authentication strategies golang"

# Search project-specific context
cd project/.synapse
python search.py "local implementation patterns"
```

### Direct Neo4j Queries
```cypher
# Find all Rust-related nodes
MATCH (n:Instruction {language: "rust"})
RETURN n.file_path, n.content

# Discover relationship patterns
MATCH (a)-[r]->(b)
WHERE a.language = "golang"
RETURN type(r), count(*)
```

## System Health

### Health Checks
```bash
# Comprehensive system status
~/.synapse-system/neo4j/activate.sh --status

# Service-specific checks
docker-compose ps
redis-cli ping
```

### BGE-M3 Performance
- **Quality**: Superior semantic understanding vs TF-IDF
- **Speed**: ~100ms per embedding (CPU)
- **Memory**: ~3GB RAM for model
- **Storage**: 8KB per 1024-dim vector

## Troubleshooting

### BGE-M3 Issues
```bash
# Test BGE-M3 directly
cd ~/.synapse-system/neo4j
python vector_engine.py "test embedding"

# Check model cache
ls ~/.cache/huggingface/hub/

# Reinstall dependencies
uv pip install --upgrade sentence-transformers
```

### Common Issues

#### Services Not Starting
```bash
# Check Docker status
sudo systemctl status docker

# Rebuild containers
docker-compose down && docker-compose up --build
```

#### Slow Search Performance
```bash
# Rebuild vector indices
python ingestion.py --rebuild-indices

# Clear and rebuild cache
redis-cli FLUSHALL
```

### Logs and Debugging
```bash
# View service logs
docker-compose logs neo4j
docker-compose logs redis

# Python ingestion logs
tail -f ~/.synapse-system/neo4j/ingestion.log
```

## Development

### Project-Specific Development

1. **Copy synapse to project**: `cp -r ~/.synapse-system project/.synapse`
2. **Use synapse-project-manager agent** to configure for your language
3. **Customize templates** in `project/.synapse/templates/`
4. **Add project-specific instructions** in `project/.synapse/instructions/`

### Performance Optimization
- Use incremental ingestion for large codebases
- Implement custom indexing strategies
- Optimize Neo4j query patterns
- Configure Redis caching policies

## Services Management

### Service URLs
- **Neo4j Browser**: http://localhost:7474
- **Neo4j Bolt**: bolt://localhost:7687
- **Redis**: localhost:6379

### Default Credentials
- **Neo4j**: neo4j / synapse_neo4j_pass
- **Redis**: No authentication (localhost only)

## Zone-0 Implementation Notes

### KISS Principle
- Start with basic file ingestion
- Add complexity only when needed
- Maintain clear separation of concerns

### Feighnburm Constant (𝔽)
Acknowledge that complex systems will exhibit emergent behaviors:
- Monitor for unexpected relationship patterns
- Document emerging usage patterns
- Plan for system evolution

### DRY and SoC
- Single source of truth for each instruction
- Clear boundaries between ingestion, storage, and retrieval
- Modular component design

## Philosophy

This system embodies the **Numogrammatic Codex** principle that in any sufficiently complex system, emergent properties will manifest. Instead of ignoring this complexity, we map it systematically, creating **zones** of understanding that enable intelligent navigation through the **currents** of information and relationships.

The **Five Whys** methodology is built into the design, encouraging deep root-cause analysis rather than surface-level solutions.

---

*"The Feighnburm Constant: Acknowledge emergent complexity, map it; never ignore it."*