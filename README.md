# Synapse System

A modular, agent-driven platform for project management, code quality, architectural design, and knowledge retrieval. Synapse integrates advanced AI agents, a unified CLI, and a knowledge engine to automate and enforce best practices across software projects.

---

## Table of Contents

- [Overview](#overview)
- [Core Components](#core-components)
- [Agent Infrastructure](#agent-infrastructure)
- [Knowledge Engine](#knowledge-engine)
- [CLI Usage](#cli-usage)
- [Development & Testing](#development--testing)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**Synapse System** is an extensible framework that combines:

- **AI-powered agents** for code review, DevOps, architecture, project management, and more
- **A knowledge engine** leveraging Neo4j, Redis, and vector search for context-rich recommendations and standards
- **A unified CLI** for orchestrating agent workflows, project setup, and system management

---

## Core Components

### 1. Unified CLI (`bin/synapse`)

- **Single entry point** for all Synapse functionality
- Context-sensitive command routing
- Manages both project-local and global operations

### 2. Project Manager (`lib/project.py`)

- Handles project initialization and agent deployment
- Manages configuration and environment setup

### 3. Update Manager (`lib/updater.py`)

- Manages agent and system updates, rollback, and version checks

### 4. Version Manager (`lib/version_manager.py`)

- Tracks agent versions, file checksums, and manifest integrity

### 5. Knowledge Engine (`.synapse/neo4j/`)

- Provides semantic, graph, and hybrid (vector+symbolic) search
- Powers standards, templates, and contextual recommendations

---

## Agent Infrastructure

Agents are the core automation building blocks in Synapse. Each agent is a self-contained Python package with modular tool support, inter-agent communication, and integrated knowledge access.

### Agent Directory Structure

```
.synapse/agents/{agent-name}/
├── {agent_name}_agent.py           # Main executable (async entry point)
├── {agent_name}_prompt.md          # System prompt/instructions
├── {agent_name}_config.yml         # Config (model, parameters, tool settings)
├── {agent_name}_state.json         # Agent memory (optional)
└── tools/
    ├── __init__.py                 # Tool loader/definition
    ├── {domain}_tools.py           # Core capabilities
    ├── synapse_integration.py      # Knowledge engine access
    ├── agent_communication.py      # Multi-agent workflow support
    └── mock_sdk.py                 # Development fallback (SDK-free)
```

#### Agent Types

- **Universal Agents:** (e.g., Project Manager, Code Hound) — cross-language automation
- **Language Specialists:** (e.g., Rust Specialist, Python Specialist) — enforce language-specific norms
- **Utility Agents:** (e.g., 4QZero, Health Check) — support, compression, and diagnostics

#### Main Agent Features

- **Async event loop:** Handles queries and orchestrates tool execution
- **@tool-decorated functions:** Modular agent capabilities (e.g., code analysis, deployment, architecture design)
- **Dynamic tool loading:** All tools are registered with an MCP server for unified execution
- **Rich inter-agent protocol:** Agents delegate, coordinate, and pass context for complex workflows

#### Example: Code Hound Agent

- Enforces TDD, SOLID, DRY, KISS principles
- Modular tool suite for analysis, standards enforcement, reporting
- Communicates with other agents for language expertise and project-wide audits

#### Example: Synapse Project Manager

- Gathers requirements & initializes projects
- Orchestrates multi-agent task breakdown and delegation
- Verifies completion and compliance with standards

---

## Knowledge Engine

- **Location:** `.synapse/neo4j/`
- **Components:** Neo4j Graph DB, Redis cache, BGE-M3 vector engine
- **Capabilities:** 
  - Hybrid search (semantic + symbolic)
  - Standards and template retrieval
  - Contextual recommendations for agents and CLI

---

## CLI Usage

After [installation](#development--testing):

```bash
synapse init .                   # Initialize project with agents and config
synapse search "code review"     # Search global knowledge base
synapse start                    # Start Synapse services (Neo4j, Redis, etc)
synapse health                   # Run system health checks
synapse manifest verify          # Verify agent versions and integrity
```

See [USAGE_GUIDE.md](USAGE_GUIDE.md) for more examples.

---

## Development & Testing

**Setup:**
```bash
git clone <repo-url>
cd synapse-system
cd .synapse/neo4j
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
docker-compose up -d
python bin/synapse version
```

**Testing:**
```bash
# Unit tests
cd .synapse/neo4j
python -m pytest tests/

# Integration tests
./test-integration.sh

# Agent integrity
python lib/version_manager.py verify
```

---

## Contributing

- See [DEVELOPMENT.md](DEVELOPMENT.md) for full technical details and architecture decisions

---

## License

[MIT](LICENSE)
