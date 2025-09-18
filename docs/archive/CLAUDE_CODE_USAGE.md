# Claude Code Integration with Synapse System

Streamlined integration between Synapse System and Claude Code with language-specific knowledge and agents.

## Quick Start

### Project Setup

**Single command initialization:**

```bash
# From any project directory
~/.synapse-system/synapse init .
```

**Example usage:**

```bash
# Rust project
cd my-rust-cli-tool/
~/.synapse-system/synapse init .

# Go web API
cd my-go-api/
~/.synapse-system/synapse init .

# TypeScript frontend
cd my-react-app/
~/.synapse-system/synapse init .
```

### What This Does

1. **Auto-detects language** from project files (Cargo.toml, package.json, go.mod, etc.)
2. **Creates language-specific agents** in `.claude/agents/`
3. **Sets up project knowledge base** in `.synapse/`
4. **Configures project context** with `.synapse.yml`
5. **Ready for immediate use** with Claude Code

### After Setup

Your project will have:

```
project/
├── .synapse/                          # Project-specific knowledge base
│   ├── instructions/                  # How-to guides and patterns
│   ├── standards/                     # Coding conventions
│   ├── templates/                     # Project templates
│   └── search capabilities            # Local search functionality
├── .claude/                           # Claude Code integration
│   ├── agents/
│   │   ├── synapse-project-manager.md # Universal project agent
│   │   └── {language}-specialist.md   # Language-specific agent
│   └── PROJECT_CONTEXT.md             # Project overview
└── .synapse.yml                       # Configuration file
```

### Using with Claude Code

After setup, invoke the agents:

```
@synapse-project-manager help me implement feature X following best practices
```

The agent now has access to:
- **Language-specific standards** (naming conventions, testing strategies)
- **Implementation patterns** (error handling, async patterns, project structure)
- **Project context** (your specific codebase and documentation)
- **Best practices** curated for your programming language

## Advanced Usage

### Global Knowledge Search

```bash
# Search across all knowledge from anywhere
~/.synapse-system/synapse search "rust error handling patterns"
~/.synapse-system/synapse search "typescript testing strategies"
~/.synapse-system/synapse search "golang microservice patterns"
```

### Service Management

```bash
# Start synapse services
~/.synapse-system/synapse start

# Check system health
~/.synapse-system/synapse status

# Stop services
~/.synapse-system/synapse stop
```

### Polyglot Projects

For projects with multiple languages, run `synapse init` in each subdirectory:

```bash
# Backend service (Rust)
cd ./backend && ~/.synapse-system/synapse init .

# Frontend app (TypeScript)
cd ./frontend && ~/.synapse-system/synapse init .

# Each subdirectory gets language-specific knowledge
```

## Supported Languages

- **Rust**: Cargo workspace, error handling, async patterns, testing strategies
- **Go**: Module management, error handling, testing, web frameworks
- **TypeScript**: Module systems, async/await, React patterns, testing
- **Zig**: Build systems, memory management
- **C**: Makefile/CMake, memory management, testing frameworks

## Agent Capabilities

The Synapse agents provide:

### Language-Aware Code Review
```
@synapse-project-manager review this Rust code for naming conventions and error handling patterns
```

### Pattern-Based Implementation
```
@rust-specialist help me implement async file processing following Rust best practices
```

### Standards Compliance
```
@synapse-project-manager check if my project structure follows Go conventions
```

### Context-Aware Guidance
```
@typescript-specialist suggest testing strategies for this React project
```

## Example Workflows

### New Feature Implementation
```
1. @synapse-project-manager I need to add authentication to this Rust web API
2. Agent searches synapse for "rust web authentication patterns"
3. Agent provides implementation following Rust conventions
4. Agent suggests testing strategies from Rust testing standards
```

### Code Review
```
1. @synapse-project-manager review this code for best practices
2. Agent checks against language-specific naming conventions
3. Agent validates error handling patterns
4. Agent suggests improvements based on templates
```

### Project Analysis
```
1. @synapse-project-manager analyze this project structure
2. Agent compares against language-specific organization standards
3. Agent identifies missing components (tests, docs, configs)
4. Agent suggests improvements following community patterns
```

## Troubleshooting

### Language Not Detected
If language detection fails, check for language indicator files:
- **Rust**: Cargo.toml
- **Go**: go.mod, go.sum
- **TypeScript**: package.json with TypeScript deps, tsconfig.json
- **Python**: pyproject.toml, requirements.txt, setup.py
- **Zig**: build.zig
- **C**: Makefile, CMakeLists.txt

### System Health Check
```bash
# Check if synapse services are running
~/.synapse-system/synapse status

# Start services if needed
~/.synapse-system/synapse start
```

### Re-initialize Project
```bash
# If setup didn't work correctly
~/.synapse-system/synapse.sh init . --force
```

This integration transforms Claude Code from a general-purpose coding assistant into a language-aware, context-rich development partner that understands both your specific project and the broader conventions of your chosen programming language.