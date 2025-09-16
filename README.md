# Synapse System: A Hybrid Intelligence Framework

A knowledge management system that provides AI agents with persistent memory, semantic search capabilities, and project-aware context through the combination of Neo4j knowledge graphs, Redis caching, and BGE-M3 vector embeddings.

## What is Synapse System?

Synapse System transforms how AI agents work with codebases by providing them with:

- **Persistent Memory**: Knowledge that survives across sessions
- **Semantic Understanding**: Deep contextual awareness using BGE-M3 embeddings
- **Project Intelligence**: Language-specific patterns and best practices
- **Contextual Search**: Hybrid graph traversal and vector similarity search
- **Self-Updating Knowledge**: Continuous learning through the OODA Loop (Observe-Orient-Decide-Act)

## Architecture Overview

```
Global Knowledge Hub (~/.synapse-system/)
├── Neo4j Knowledge Graph    # Relationships and structured data
├── Redis Cache             # Fast query responses
├── BGE-M3 Vector Store     # 1024-dimensional semantic embeddings
└── Language Templates      # Rust, Go, TypeScript, Python patterns

Project Integration
├── .claude/agents/         # Language-specific AI agents
├── .synapse/              # Project knowledge base
└── .synapse.yml           # Configuration
```

## Key Features

### 🧠 **Hybrid Intelligence**
- Combines structured knowledge graphs with semantic vector search
- Local BGE-M3 embeddings (no API keys required)
- Redis caching for sub-second response times

### 🔧 **Language-Aware**
- Automatic project language detection (Rust, Go, TypeScript, Python, Zig, C)
- Language-specific coding standards and patterns
- Context-aware code generation and review

### 🤖 **Agent Integration**
- Seamless Claude Code integration
- Specialized agents for different programming languages
- Project-aware context and recommendations

### 📚 **Knowledge Persistence**
- Long-term memory across development sessions
- Accumulates project-specific wisdom over time
- Global knowledge base with community best practices

## Use Cases

- **Code Review**: AI agents understand your project's patterns and conventions
- **Feature Implementation**: Context-aware suggestions that fit your architecture
- **Documentation**: Agents know your project structure and can write appropriate docs
- **Refactoring**: Intelligent suggestions based on your existing codebase patterns
- **Learning**: New team members get AI assistance trained on your specific codebase

## Technical Architecture

### System Components

```
~/.synapse-system/
├── .synapse/neo4j/             # Core system engine
│   ├── context_manager.py      # Hybrid search API
│   ├── vector_engine.py        # BGE-M3 embeddings
│   ├── ingestion.py            # Knowledge graph builder
│   └── synapse_search.py       # Agent integration
├── instructions/               # How-to guides and patterns
├── standards/                  # Coding conventions
├── templates/                  # Project boilerplate
└── synapse                     # Unified CLI tool
```

### Service Infrastructure

- **Neo4j**: Knowledge graph (localhost:7474, bolt://localhost:7687)
- **Redis**: Query cache (localhost:6379)
- **BGE-M3**: Local semantic embeddings (~2.3GB model)
- **SQLite**: Vector storage for embeddings

## Core Principles

Following the **Numogrammatic Codex**:

- **KISS**: Keep implementations simple, reduce complexity
- **DRY**: Single source of truth for each instruction
- **SoC**: Clean separation between ingestion, storage, and retrieval
- **TDD**: Test-driven development approach
- **Five Whys**: Root cause analysis methodology
- **OODA Loop**: Observe-Orient-Decide-Act for self-updating systems

## Getting Started

### Quick Setup
```bash
# Start the system
~/.synapse-system/synapse start

# Initialize your project
cd your-project/
~/.synapse-system/synapse init .

# Use with Claude Code
@synapse-project-manager help with this project
```

For detailed installation and setup instructions, see **[SETUP_GUIDE.md](SETUP_GUIDE.md)**.

For Claude Code integration details, see **[CLAUDE_CODE_USAGE.md](CLAUDE_CODE_USAGE.md)**.

For architectural deep-dive, see **[LANGUAGE_ARCHITECTURE.md](LANGUAGE_ARCHITECTURE.md)**.

## Requirements

- **Python 3.12+** with uv package manager
- **Docker & Docker Compose** for services
- **~3GB disk space** for BGE-M3 model and data
- **4GB+ RAM** recommended for optimal performance

## Philosophy

*"The Feighnburm Constant: In any sufficiently complex system, emergent properties will manifest. Acknowledge it, map it; never ignore it."*

Synapse System embraces complexity rather than fighting it, creating systematic approaches to navigate the currents of knowledge and relationships in software development.