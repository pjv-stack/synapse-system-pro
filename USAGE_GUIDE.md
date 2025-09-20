# Synapse Usage Guide

Quick guide for using Synapse with your projects.

## Getting Started

**Already installed?** Skip to [Project Setup](#project-setup)

**Need to install?**
```bash
git clone https://github.com/your-repo/synapse-system.git ~/.synapse-system
cd ~/.synapse-system && ./install.sh
```

**Having issues?** Run `synapse doctor --fix`

## Project Setup

```bash
# In any project directory
cd my-project/
synapse init .

# This auto-detects your language and sets up agents
```

### Using Agents with Claude Code

```
@synapse-project-manager help me implement user authentication
@rust-specialist write error handling following our patterns
@code-hound review this code for quality issues
```

## Essential Commands

```bash
# Fix any issues automatically
synapse doctor --fix

# Set up project
synapse init .

# Search for code patterns
synapse search "rust error handling"

# Check system health
synapse status

# Update agents to latest version
synapse update
```

## What Gets Created

After `synapse init .`, your project gets:

```
project/
├── .claude/agents/          # AI agents for Claude Code
│   ├── synapse-project-manager.md
│   ├── rust-specialist.md   # (or your language)
│   └── code-hound.md        # Code quality checker
└── .synapse.yml             # Configuration
```

**Multi-language projects:** Run `synapse init .` in each language directory.

## Available Agents

**Universal (every project):**
- `@synapse-project-manager` - Coordinates complex tasks
- `@code-hound` - Code quality and best practices
- `@git-workflow` - Git operations and PRs

**Language specialists:**
- `@rust-specialist` - Rust patterns and conventions
- `@typescript-specialist` - TypeScript/React development
- `@golang-specialist` - Go development patterns
- `@python-specialist` - Python conventions

**Best practice:** Start with `@synapse-project-manager` for complex features.

## Keeping Updated

```bash
# Check for agent updates
synapse update

# Auto-apply updates
synapse update -y
```

## Common Tasks

**Search for patterns:**
```bash
synapse search "rust error handling"
synapse search "async patterns"
```

**Get help:**
```bash
synapse doctor --fix     # Fix issues automatically
synapse manifest list    # See all available agents
```

## Troubleshooting

**Most issues are fixed automatically:**
```bash
synapse doctor --fix
```

**If services won't start:**
```bash
# Make sure Docker is running
docker --version

# Restart everything
synapse stop && synapse start
```

**Need more help?**
- Run `synapse status` to see what's wrong
- Check [DEVELOPMENT.md](DEVELOPMENT.md) for technical details