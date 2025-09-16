# Language-Specific Synapse System Architecture

A comprehensive guide to the multi-language, project-aware Synapse System that provides contextual knowledge for different programming languages and project types.

## Overview

The Enhanced Synapse System now supports language-specific knowledge bases that can be ported into individual projects or different parts of polyglot applications. Each language template contains specialized instructions, standards, and templates relevant to that specific programming ecosystem.

## Architecture Design

### Global Knowledge Hub
```
~/.synapse-system/
├── neo4j/                      # Core synapse engine
├── languages/                  # Language-specific templates
│   ├── rust/
│   │   ├── instructions/      # Rust-specific how-to guides
│   │   ├── standards/         # Rust coding conventions
│   │   └── templates/         # Rust project templates
│   ├── golang/
│   ├── typescript/
│   ├── zig/
│   └── c/
├── deploy/                     # Deployment and sync tools
└── tools/                      # Claude Code integration
```

### Project-Local Installation
```
project-directory/
├── .synapse/                   # Project-specific synapse
│   ├── instructions/          # Language + project knowledge
│   ├── standards/             # Applicable coding standards
│   ├── templates/             # Relevant templates
│   ├── config.json           # Project configuration
│   ├── search.py             # Local search interface
│   └── ingest.py             # Project ingestion
├── src/                       # Project source code
├── Cargo.toml                 # Language-specific files
└── README.md
```

## Supported Languages

### Rust
**Detection**: `Cargo.toml`, `*.rs` files
**Template Location**: `~/.synapse-system/languages/rust/`

**Includes**:
- Cargo workspace management
- Error handling patterns with `anyhow` and `thiserror`
- Async runtime patterns with Tokio
- Naming conventions following community standards
- Testing strategies with comprehensive examples

### Go
**Detection**: `go.mod`, `go.sum`, `*.go` files
**Template Location**: `~/.synapse-system/languages/golang/`

**Ready for**: Module management, error handling, testing patterns, naming conventions

### TypeScript
**Detection**: `package.json` with TypeScript dependencies, `tsconfig.json`
**Template Location**: `~/.synapse-system/languages/typescript/`

**Ready for**: Module systems, async patterns, testing with Jest/Vitest, React patterns

### Zig
**Detection**: `build.zig`
**Template Location**: `~/.synapse-system/languages/zig/`

**Ready for**: Build system patterns, memory management, testing

### C
**Detection**: `Makefile`, `CMakeLists.txt`
**Template Location**: `~/.synapse-system/languages/c/`

**Ready for**: Build systems, memory management, testing frameworks

## Usage Workflows

### Single Language Project Setup

```bash
# Initialize Rust project
cd my-rust-project/
~/.synapse-system/synapse init .

# Result: .synapse/ directory with Rust-specific knowledge
```

### Polyglot Project Setup

```bash
# Backend in Rust
cd backend/
~/.synapse-system/synapse init .

# Frontend in TypeScript
cd ../frontend/
~/.synapse-system/synapse init .

# Result:
# backend/.synapse/     (Rust knowledge)
# frontend/.synapse/    (TypeScript knowledge)
```

### Microservices Architecture

```bash
# API Gateway in Go
cd services/gateway/
~/.synapse-system/synapse init .

# User Service in Rust
cd ../user/
~/.synapse-system/synapse init .

# Web UI in TypeScript
cd ../../web/
~/.synapse-system/synapse init .
```

## Claude Code Integration

### Enhanced Project Manager Agent

The system includes an enhanced project manager agent at:
`~/.synapse-system/tools/synapse-project-manager.md`

**New Capabilities**:
- Language detection from project structure
- Context-aware task verification
- Standards compliance checking
- Template-based validation

**Available Tools**:
- `SynapseSearch` - Search knowledge base with language context
- `SynapseStandard` - Retrieve specific coding standards
- `SynapseTemplate` - Access project templates
- `SynapseHealth` - Check system health

### Tool Usage Examples

```python
# From Claude Code agent
from synapse_tools import SynapseTools

tools = SynapseTools()

# Search for Rust error handling patterns
result = tools.search("error handling", language_context="rust")

# Get Rust naming conventions
standard = tools.get_standard("naming-conventions", "rust")

# Health check
health = tools.health_check()
```

## Project Configuration

### Language Detection
The system automatically detects project language based on:

- **Rust**: `Cargo.toml` presence
- **Go**: `go.mod` or `go.sum` presence
- **TypeScript**: `package.json` with TypeScript dependencies
- **Zig**: `build.zig` presence
- **C**: `Makefile` or `CMakeLists.txt` presence

### Configuration File
Each project synapse includes a `config.json`:

```json
{
    "project_name": "my-rust-project",
    "language": "rust",
    "synapse_version": "2.0.0",
    "created_at": "2025-09-16T13:21:10+10:00",
    "global_sync_enabled": false,
    "vector_model": "simple_tfidf",
    "cache_ttl": 3600
}
```

## Knowledge Management

### Search Global Knowledge
```bash
# Search across all knowledge from anywhere
~/.synapse-system/synapse search "rust error handling patterns"
~/.synapse-system/synapse search "typescript testing strategies"
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

## Content Organization

### Instructions (How-To Guides)
- **Purpose**: Step-by-step implementation guidance
- **Examples**: "cargo-workspace.md", "error-handling.md", "async-runtime.md"
- **Format**: Markdown with code examples and best practices

### Standards (Coding Conventions)
- **Purpose**: Language-specific coding standards and conventions
- **Examples**: "naming-conventions.md", "testing-strategy.md", "module-structure.md"
- **Format**: Comprehensive guidelines with examples and anti-patterns

### Templates (Project Boilerplate)
- **Purpose**: Starter templates for common project types
- **Examples**: "cli-app/", "web-api/", "library/"
- **Format**: Directory structures with sample code

## Integration Scenarios

### Scenario 1: New Rust CLI Application

```bash
# Initialize project
cargo new my-cli-tool
cd my-cli-tool

# Add synapse
~/.synapse-system/synapse init .

# Agent can now access:
# - Rust CLI patterns from templates
# - Error handling standards
# - Testing strategies
# - Cargo workspace management
```

### Scenario 2: Web Application Stack

```bash
# Project structure
web-app/
├── api/          # Rust backend
├── web/          # TypeScript frontend
└── shared/       # Common utilities

# Initialize each component
cd api && ~/.synapse-system/synapse init .
cd ../web && ~/.synapse-system/synapse init .

# Result: Language-specific knowledge in each subdirectory
```

### Scenario 3: Cross-Language Development

When working across multiple languages, each `.synapse/` installation provides:

1. **Language-Specific Context**: Relevant patterns and conventions
2. **Local Knowledge**: Project-specific accumulated wisdom
3. **Global Sync**: Latest community best practices
4. **Tool Integration**: Claude Code agents with context awareness

## Development Workflow

### For Developers

1. **Project Setup**: Run initialization script for target language
2. **Daily Usage**: Claude Code agents automatically use local synapse
3. **Knowledge Updates**: Periodic sync with global knowledge base
4. **Contribution**: Share valuable patterns back to global repository

### For Claude Code Agents

1. **Language Detection**: Automatically detect project context
2. **Context Retrieval**: Search relevant knowledge for current language
3. **Standards Validation**: Check code against language conventions
4. **Template Matching**: Compare implementations against best practices

## Performance Considerations

### Local vs Global

- **Local Synapse**: Fast access, project-specific, lightweight
- **Global Synapse**: Comprehensive, shared, requires full infrastructure
- **Hybrid Approach**: Local for speed, global for comprehensive knowledge

### Resource Usage

- **Storage**: Each language template ~1-5MB
- **Memory**: Minimal impact, lazy loading of knowledge
- **Network**: Only during sync operations

## Extension and Customization

### Adding New Languages

1. Create language directory structure
2. Populate with instructions, standards, templates
3. Update detection logic in initialization script
4. Test with sample project

### Custom Standards

1. Add language-specific standards to local synapse
2. Test and validate with projects
3. Contribute valuable standards back to global
4. Share across team via sync mechanism

## Troubleshooting

### Common Issues

**Language Not Detected**
- Check for language-specific files (Cargo.toml, package.json, etc.)
- Use explicit `--language` flag during initialization

**Synapse Not Found**
- Verify `.synapse/` directory exists in project or parent directories
- Re-run initialization if needed

**Search Not Working**
- Check synapse health with `python synapse_tools.py health`
- Verify dependencies are installed in `.synapse/.venv/`

**Outdated Knowledge**
- Run sync to pull latest global updates
- Check sync status to see last update time

### Debug Commands

```bash
# Check synapse health
~/.synapse-system/synapse status

# Test search functionality
~/.synapse-system/synapse search "rust patterns"

# Start services if needed
~/.synapse-system/synapse start

# Re-initialize project
~/.synapse-system/synapse init . --force
```

## Future Enhancements

### Planned Features

1. **Real-time Knowledge Sharing**: Live sync between team members
2. **AI-Enhanced Content**: Automatic pattern extraction from codebases
3. **Cross-Language Patterns**: Common patterns that apply across languages
4. **Integration Metrics**: Track knowledge usage and effectiveness
5. **Template Marketplace**: Community-contributed templates and patterns

### Extensibility

The architecture is designed for easy extension:

- **New Languages**: Add template directories and detection logic
- **Custom Tools**: Extend synapse_tools.py with new capabilities
- **Advanced Search**: Integrate ML models for better semantic search
- **Team Knowledge**: Private knowledge repositories for organizations

This language-specific architecture transforms the Synapse System from a monolithic knowledge base into a flexible, contextual intelligence platform that adapts to different programming languages and project structures while maintaining the benefits of shared knowledge and best practices.