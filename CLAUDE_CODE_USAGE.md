# Claude Code Integration with Synapse System

Simple, one-command setup to make any project Claude Code ready with language-specific knowledge.

## Quick Start

### For Project Managers or Agents

**Single command setup:**

```bash
# From any project directory
~/.synapse-system/setup "your project description"
```

**Example usage:**

```bash
# Rust project
cd my-rust-cli-tool/
~/.synapse-system/setup "CLI tool for file processing with async I/O"

# Go web API
cd my-go-api/
~/.synapse-system/setup "REST API server with authentication"

# TypeScript frontend
cd my-react-app/
~/.synapse-system/setup "React application with TypeScript"
```

### What This Does

1. **Auto-detects language** from project files (Cargo.toml, package.json, go.mod, etc.)
2. **Installs language-specific synapse** with relevant standards and patterns
3. **Sets up Claude Code agents** in `.claude-code/agents/`
4. **Creates project context** with usage instructions
5. **Ready for immediate use** with Claude Code

### After Setup

Your project will have:

```
project/
├── .synapse/                           # Language-specific knowledge base
│   ├── instructions/                   # How-to guides (error handling, async, etc.)
│   ├── standards/                      # Coding conventions and best practices
│   └── search.py                       # Local search tool
├── .claude-code/                       # Claude Code integration
│   ├── agents/
│   │   └── synapse-project-manager.md # Enhanced project manager agent
│   └── PROJECT_CONTEXT.md             # Project information and usage guide
└── your-project-files...
```

### Using with Claude Code

After setup, simply use:

```
@claude-code/agents/synapse-project-manager.md help me implement feature X following Rust best practices
```

The agent now has access to:
- **Language-specific standards** (naming conventions, testing strategies)
- **Implementation patterns** (error handling, async patterns, project structure)
- **Project context** (your specific codebase and documentation)
- **Best practices** curated for your programming language

## Advanced Usage

### Manual Language Selection

```bash
# Force specific language
~/.synapse-system/deploy/simple-setup.sh . golang "microservice API"
~/.synapse-system/deploy/simple-setup.sh . typescript "React component library"
```

### Polyglot Projects

```bash
# Backend service
~/.synapse-system/deploy/simple-setup.sh ./backend rust "API server"

# Frontend app
~/.synapse-system/deploy/simple-setup.sh ./frontend typescript "Web interface"

# Each subdirectory gets language-specific knowledge
```

### Search Project Knowledge

```bash
# Search for patterns in your project's synapse
cd .synapse && python search.py "error handling patterns"
cd .synapse && python search.py "async testing strategies"
cd .synapse && python search.py "project structure conventions"
```

## Supported Languages

- **Rust**: Cargo workspace, error handling, async patterns, testing strategies
- **Go**: Module management, error handling, testing, web frameworks
- **TypeScript**: Module systems, async/await, React patterns, testing
- **Zig**: Build systems, memory management
- **C**: Makefile/CMake, memory management, testing frameworks

## Agent Capabilities

The enhanced project manager agent can now:

### Language-Aware Code Review
```
@claude-code/agents/synapse-project-manager.md review this Rust code for naming conventions and error handling patterns
```

### Pattern-Based Implementation
```
@claude-code/agents/synapse-project-manager.md help me implement async file processing following Rust best practices
```

### Standards Compliance
```
@claude-code/agents/synapse-project-manager.md check if my project structure follows Go conventions
```

### Context-Aware Guidance
```
@claude-code/agents/synapse-project-manager.md suggest testing strategies for this TypeScript React project
```

## Example Workflows

### New Feature Implementation
```
1. @claude-code/agents/synapse-project-manager.md I need to add authentication to this Rust web API
2. Agent searches synapse for "rust web authentication patterns"
3. Agent provides implementation following Rust conventions
4. Agent suggests testing strategies from Rust testing standards
```

### Code Review
```
1. @claude-code/agents/synapse-project-manager.md review this code for best practices
2. Agent checks against language-specific naming conventions
3. Agent validates error handling patterns
4. Agent suggests improvements based on templates
```

### Project Analysis
```
1. @claude-code/agents/synapse-project-manager.md analyze this project structure
2. Agent compares against language-specific organization standards
3. Agent identifies missing components (tests, docs, configs)
4. Agent suggests improvements following community patterns
```

## Troubleshooting

### Language Not Detected
```bash
# Check what would be detected
~/.synapse-system/deploy/simple-setup.sh . auto

# Force specific language
~/.synapse-system/deploy/simple-setup.sh . rust "description"
```

### Update Knowledge
```bash
# Sync with latest global patterns
~/.synapse-system/deploy/sync-global.sh pull
```

### Check System Health
```bash
python ~/.synapse-system/tools/synapse_tools.py health
```

This integration transforms Claude Code from a general-purpose coding assistant into a language-aware, context-rich development partner that understands both your specific project and the broader conventions of your chosen programming language.