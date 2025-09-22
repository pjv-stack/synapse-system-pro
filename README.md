# Synapse System

Give your AI assistant a memory that remembers your coding patterns, project structure, and team conventions. Synapse creates intelligent, context-aware AI agents that understand your codebase.

## Quick Install

```bash
# 1. Clone and install
git clone https://github.com/sub0xdai/synapse-system.git ~/.synapse-system
cd ~/.synapse-system && ./install.sh

```

**Requirements:** Python 3.12+, Docker 

**First run takes ~5 minutes** (downloads AI model), then it's instant.

## Quick Start

```bash
# In any project directory
cd my-project/
synapse init .

# Now use with Claude Code (examples)
@synapse-project-manager help me implement user authentication
@rust-specialist write error handling following our patterns
```

## What It Does

Instead of explaining your project patterns every time, Synapse gives AI:
- **Memory of your conventions** - Naming, architecture, testing patterns
- **Understanding of your codebase** - Existing functions, error handling, dependencies
- **Language-specific knowledge** - Best practices for Rust, TypeScript, Go, Python
- **Smart search** - Finds relevant code by meaning, not just keywords

## Essential Commands

```bash
synapse doctor           # Fix any issues automatically
synapse init .           # Set up current project
synapse search "query"   # Find code by meaning
synapse status          # Check if everything's running
```

**Troubleshooting:** Run `synapse doctor --fix` to auto-resolve most issues.


## How It Works

- **Knowledge Graph** (Neo4j) - Stores relationships between code, patterns, and conventions
- **Vector Search** (BGE-M3) - Finds semantically similar code across your projects
- **Specialized Agents** - Language experts (Rust, TypeScript, Go, Python) with context
- **Smart Caching** (Redis) - Fast access to frequently used patterns

**Need Help?**
Check [USAGE_GUIDE.md](USAGE_GUIDE.md) for detailed examples.
