# Synapse System

A hybrid intelligence framework that provides AI agents with persistent memory, semantic search, and project-aware context through Neo4j knowledge graphs, Redis caching, and BGE-M3 vector embeddings.

## What is Synapse System?

Synapse transforms how AI agents work with codebases by providing:

- **Persistent Memory**: Knowledge that survives across sessions
- **Semantic Understanding**: Deep contextual awareness using BGE-M3 embeddings
- **Project Intelligence**: Language-specific patterns and best practices
- **Smart Updates**: Version tracking and agent update system
- **Unified CLI**: Single `synapse` command for all functionality

## ⚡ Quick Start

```bash
# 1. Start synapse services
synapse start

# 2. Initialize your project
cd your-project/
synapse init .

# 3. Search global knowledge
synapse search "rust error handling"
```

## 🎯 Features

- **Language Detection**: Auto-detects Rust, Go, TypeScript, Python, Zig, C
- **Intelligent Search**: Intent-aware with query expansion and smart ranking
- **Smart Agents**: Context-aware AI agents with project knowledge
- **Update System**: `synapse update` keeps projects current
- **Flexible Deployment**: Copy agents (stable) or symlink (auto-update)
- **Integrity Checks**: Verify agents haven't been corrupted

## 📁 What Gets Created

After `synapse init`, your project has:

```
project/
├── .claude/agents/              # AI agents for Claude Code
│   ├── synapse-project-manager.md
│   ├── {language}-specialist.md
│   ├── code-hound.md           # Quality enforcement
│   ├── git-workflow.md         # Git operations
│   └── test-runner.md          # Test execution
└── .synapse.yml                # Configuration & versions
```

## 🤖 Using with Claude Code

```
@synapse-project-manager help me implement feature X following best practices
@rust-specialist implement error handling
@code-hound review my code for quality issues
```

## 🔧 Architecture

```
Global Knowledge Hub (~/.synapse-system/)
├── bin/synapse              # Unified CLI
├── lib/                     # Python modules
├── .synapse/
│   ├── neo4j/              # Knowledge graph engine
│   ├── agents/             # Agent definitions (16 total)
│   └── VERSION             # System version
└── synapse.sh              # Legacy wrapper
```

**Services:**
- **Neo4j**: Knowledge graph (localhost:7474)
- **Redis**: Query cache (localhost:6379)
- **BGE-M3**: 1024-dimensional semantic vectors

## 📚 Documentation

- **[USAGE_GUIDE.md](USAGE_GUIDE.md)** - Complete user guide with all commands
- **[DEVELOPMENT.md](DEVELOPMENT.md)** - Technical architecture and development
- **[CHANGELOG.md](CHANGELOG.md)** - Version history and changes

## 💡 Use Cases

- **Code Review**: AI agents understand your project's patterns
- **Feature Implementation**: Context-aware suggestions that fit your architecture
- **Knowledge Retention**: Team wisdom persists across projects
- **Onboarding**: New developers get AI assistance trained on your codebase

## 🛠️ System Requirements

- Python 3.12+ with `uv` package manager
- Docker & Docker Compose
- ~2.3GB for BGE-M3 model (auto-downloads)

## ⚡ All Commands

```bash
# Service management
synapse start/stop/status

# Project management
synapse init [dir] [--link]
synapse update [dir] [-y]

# Knowledge access
synapse search <query>
synapse standards <name> [lang]
synapse template <name>

# System management
synapse version
synapse manifest list/verify/info
synapse health
```

## 🔄 Updates

Keep your projects current:

```bash
synapse update          # Update current project
synapse update /path    # Update specific project
synapse update -y       # Auto-approve updates
```

---

**Ready to start?** See the [USAGE_GUIDE.md](USAGE_GUIDE.md) for detailed instructions.