# Synapse System - Usage Guide

Complete guide to using Synapse System for AI-powered development with persistent knowledge and context-aware agents.

## Table of Contents

- [Installation & Setup](#installation--setup)
- [Quick Start](#quick-start)
- [Command Reference](#command-reference)
- [Project Management](#project-management)
- [Agent Usage](#agent-usage)
- [Update System](#update-system)
- [Advanced Features](#advanced-features)
- [Troubleshooting](#troubleshooting)

## Installation & Setup

### Prerequisites

```bash
# Check Python version (need 3.12+)
python3 --version

# Check Docker
docker --version

# Install uv package manager (if needed)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### First-Time Setup

```bash
# 1. Start synapse services (Neo4j + Redis)
synapse start

# This will:
# - Start Docker containers
# - Download BGE-M3 model (~2.3GB, first time only)
# - Initialize knowledge base
```

### Verify Installation

```bash
# Check system status
synapse status

# Test search functionality
synapse search "test query"

# Check version
synapse version
```

## Quick Start

### Initialize a Project

```bash
# Navigate to your project
cd my-rust-project/

# Initialize with synapse
synapse init .

# What this does:
# 1. Detects language (Rust, Go, TypeScript, Python, etc.)
# 2. Creates .claude/agents/ with AI agents
# 3. Creates .synapse.yml configuration
# 4. Ready for Claude Code integration
```

### Use with Claude Code

```
# Ask the project manager for help
@synapse-project-manager help me implement user authentication

# Get language-specific assistance
@rust-specialist implement error handling for HTTP requests

# Review code quality
@code-hound review this function for SOLID principles

# Handle git operations
@git-workflow create feature branch for user-auth
```

## Command Reference

### Service Management

```bash
# Start synapse services
synapse start

# Stop synapse services
synapse stop

# Check service health
synapse status
```

### Project Management

```bash
# Initialize current directory
synapse init .

# Initialize specific directory
synapse init /path/to/project

# Use symlinks (auto-updating agents)
synapse init . --link

# Update project agents
synapse update

# Update specific project
synapse update /path/to/project

# Auto-approve updates
synapse update -y
```

### Knowledge Access

```bash
# Search global knowledge
synapse search "rust error handling patterns"
synapse search "typescript testing strategies"

# Get coding standards
synapse standards naming-conventions rust
synapse standards testing-strategy python

# Access templates
synapse template web-api
synapse template cli-app
```

### System Management

```bash
# Show version information
synapse version

# Health check
synapse health

# Ingest knowledge
synapse ingest
synapse ingest --force

# Manage agent manifest
synapse manifest list
synapse manifest verify rust-specialist
synapse manifest info synapse-project-manager
```

### Direct Tool Access (Advanced)

```bash
# Direct tool access for debugging
synapse tool search "query"
synapse tool standard "naming-conventions" "rust"
synapse tool template "web-api"
synapse tool health
```

## Project Management

### Project Structure

After initialization, your project contains:

```
project/
├── .claude/
│   └── agents/
│       ├── synapse-project-manager.md    # Universal project agent
│       ├── {language}-specialist.md      # Language-specific agent
│       ├── code-hound.md                 # Code quality enforcer
│       ├── git-workflow.md               # Git operations
│       ├── test-runner.md                # Test execution
│       └── file-creator.md               # File/template creation
└── .synapse.yml                          # Configuration & versions
```

### Configuration File (.synapse.yml)

```yaml
version: "1.0"
language: "rust"
synapse_version: "2024.1.0"
project_name: "my-project"
deployment_method: "copy"  # or "symlink"

agent_versions:
  synapse-project-manager: "1758105430.ca551cb5"
  rust-specialist: "1758107914.627812e8"
  code-hound: "1758106678.4ac9ced9"
  # ... other agents

knowledge_paths:
  - "./docs"
  - "./README.md"
  - "./CHANGELOG.md"

created_at: "2024-09-18T13:50:05.815554"
updated_at: "2024-09-18T13:50:05.815566"
```

### Language Detection

Synapse automatically detects your project language:

| Language   | Detection Files                          |
|------------|------------------------------------------|
| Rust       | `Cargo.toml`                            |
| Go         | `go.mod`                                 |
| TypeScript | `package.json`                          |
| Python     | `pyproject.toml`, `requirements.txt`    |
| Zig        | `build.zig`                             |
| C/C++      | `Makefile`, `CMakeLists.txt`            |

### Polyglot Projects

For multi-language projects, initialize each directory:

```bash
# Backend service (Rust)
cd ./backend && synapse init .

# Frontend app (TypeScript)
cd ./frontend && synapse init .

# Python utilities
cd ./scripts && synapse init .
```

## Agent Usage

### Available Agents

#### Universal Agents (All Projects)
- **synapse-project-manager**: Task coordination and project management
- **code-hound**: Enforces TDD, SOLID, KISS, DRY principles
- **git-workflow**: Handles branches, commits, PRs
- **test-runner**: Executes tests and analyzes failures
- **file-creator**: Creates files and applies templates

#### Language-Specific Agents
- **rust-specialist**: Rust development patterns
- **typescript-specialist**: TypeScript/React patterns
- **golang-specialist**: Go development patterns
- **python-specialist**: Python development patterns

### Agent Capabilities

Each agent has access to:
- **SynapseSearch**: Search global knowledge base
- **SynapseStandard**: Get language-specific standards
- **SynapseTemplate**: Access project templates
- **SynapseHealth**: Check system health

### Best Practices

1. **Start with Project Manager**: `@synapse-project-manager` for complex tasks
2. **Use Language Specialists**: For language-specific implementation
3. **Quality Checks**: `@code-hound` for rigorous code review
4. **Git Operations**: `@git-workflow` for branch management and PRs

## Update System

### Why Updates Matter

Synapse agents evolve with:
- New language patterns
- Updated best practices
- Bug fixes and improvements
- New tool integrations

### Copy vs Symlink Deployment

#### Copy Deployment (Default)
```bash
synapse init .
```
- **Pros**: Stable, controlled updates
- **Cons**: Manual updates required
- **Use when**: Production projects, stable environments

#### Symlink Deployment
```bash
synapse init . --link
```
- **Pros**: Automatic updates, bleeding-edge features
- **Cons**: Changes without notice
- **Use when**: Development, experimental projects

### Update Workflow

```bash
# Check for updates
synapse update

# Example output:
# 📦 Found 3 updates:
#    • rust-specialist: 1758107914.627812e8 → 1758108120.4b3b303d
#    • code-hound: 1758106678.4ac9ced9 → 1758106800.5bd4fed2
#    • system: 2024.1.0 → 2024.1.1

# Apply updates with confirmation
synapse update

# Auto-approve updates
synapse update -y

# Update specific project
synapse update /path/to/project
```

### Version Tracking

Each agent has a version based on:
- **Timestamp**: When it was last modified
- **Checksum**: Content hash for integrity

Example: `1758107914.627812e8`
- `1758107914`: Unix timestamp
- `627812e8`: 8-character content hash

## Advanced Features

### Global Knowledge Search

```bash
# Enhanced search with intelligent query processing
synapse search "rust error handling"          # Auto-detects debugging intent
synapse search "how to implement async"       # Detects implementation intent
synapse search "python test coverage"         # Detects testing intent
synapse search "optimize database queries"    # Detects optimization intent

# Fuzzy search handles typos
synapse search "errror handeling"            # Still finds error handling
synapse search "authentiction securityy"      # Finds authentication security
```

### Standards and Templates

```bash
# Get naming conventions
synapse standards naming-conventions rust
synapse standards module-structure typescript

# Access templates
synapse template cli-app rust
synapse template web-api golang
synapse template component typescript
```

### Manifest Management

```bash
# List all agents with versions
synapse manifest list

# Verify agent integrity
synapse manifest verify rust-specialist
synapse manifest verify  # all agents

# Get detailed agent info
synapse manifest info synapse-project-manager

# Update manifest (after changes)
synapse manifest update
```

### Custom Knowledge Paths

Edit `.synapse.yml` to include project-specific knowledge:

```yaml
knowledge_paths:
  - "./docs"
  - "./README.md"
  - "./CONTRIBUTING.md"
  - "./architecture/*.md"
  - "./specs/*.md"
```

## Troubleshooting

### Services Not Starting

```bash
# Check Docker is running
docker --version
sudo systemctl start docker  # Linux
open -a Docker              # macOS

# Restart services
synapse stop
synapse start

# Check logs
docker logs synapse-neo4j
docker logs synapse-redis
```

### Agent Issues

```bash
# Verify agent integrity
synapse manifest verify

# Re-initialize project
synapse init . --force

# Check system health
synapse health
```

### Search Not Working

```bash
# Check services
synapse status

# Manual ingestion
synapse ingest --force

# Test with simple query
synapse search "test"
```

### Update Failures

```bash
# Check current versions
synapse version

# Force update
synapse update -y

# Manual agent sync (if needed)
cp ~/.synapse-system/.synapse/agents/*.md .claude/agents/
```

### Permission Issues

```bash
# Check directory permissions
ls -la .claude/
ls -la .synapse.yml

# Fix permissions
chmod 755 .claude/
chmod 644 .synapse.yml
```

### Legacy Projects

For projects created with old versions:

```bash
# Check if migration needed
synapse update

# If migration required, run:
synapse init . --force
```

## Performance Tips

1. **Use Local Cache**: Services cache results for faster responses
2. **Specific Queries**: More specific searches return better results
3. **Symlink for Dev**: Use `--link` for active development
4. **Batch Updates**: Update multiple projects with scripts
5. **Health Checks**: Regular `synapse health` prevents issues

## Getting Help

- **Command Help**: `synapse --help`
- **Specific Command**: `synapse init --help`
- **Agent Issues**: `synapse manifest verify`
- **System Status**: `synapse status`
- **Version Info**: `synapse version`

For more technical details, see [DEVELOPMENT.md](DEVELOPMENT.md).