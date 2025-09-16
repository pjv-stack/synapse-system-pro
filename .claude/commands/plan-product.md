# Plan Product - Synapse-Powered Project Setup

Plan a new product with Synapse System integration for intelligent context retrieval and knowledge-driven development.

## Project Initialization Workflow

### 1. Requirements Gathering
Use the project-manager agent to conduct interactive requirements analysis:
```
@project-manager

Please help me plan a new project. I need to gather requirements and set up the development environment with Synapse integration.
```

The agent will ask key questions:
- **Application Type**: CLI tool, Web app, API service, Library, etc.
- **Primary Language**: Rust, Go, TypeScript, Python, Zig, C
- **Performance Requirements**: Latency targets, throughput needs
- **Scale Expectations**: User count, request volume
- **Security Needs**: Authentication, encryption, compliance
- **Integration Requirements**: Databases, external APIs, services

### 2. Synapse System Activation
Ensure the global Synapse system is operational:
```bash
# Activate and verify Synapse system health
@neo4j/activate.sh --status

# Force system activation if needed
@neo4j/activate.sh --force
```

### 3. Project Setup Commands
```bash
# Navigate to your project directory
cd /path/to/your/project

# Copy Synapse system to project
cp -r ~/.synapse-system/.synapse .

# Initialize project-specific Synapse
cd .synapse
@neo4j/ingestion.py --project-init

# Verify health
@neo4j/context_manager.py --health
```

### 4. Language-Specific Configuration
The system will auto-detect your project language and configure appropriately:

**For Rust projects**:
```bash
@neo4j/synapse_search.py "rust project templates"
@neo4j/synapse_search.py "cargo workspace patterns"
```

**For Go projects**:
```bash
@neo4j/synapse_search.py "golang project structure"
@neo4j/synapse_search.py "go module patterns"
```

**For TypeScript projects**:
```bash
@neo4j/synapse_search.py "typescript project setup"
@neo4j/synapse_search.py "npm workspace patterns"
```

### 5. Knowledge Base Population
```bash
# Ingest project documentation and code
cd .synapse
@neo4j/ingestion.py --project /path/to/project

# Verify ingestion
@neo4j/context_manager.py "project patterns"
```

### 6. Development Environment Verification
```bash
# Check all services are running
@neo4j/activate.sh --status

# Test semantic search
@neo4j/synapse_search.py "development setup"

# Verify vector embeddings
@neo4j/vector_engine.py --test-embedding "hello world"
```

## Available Synapse Scripts by Category

### Project Initialization Scripts (deploy/)
- `@deploy/init-project.sh --language rust` - Initialize language-specific Synapse for project
- `@deploy/setup-claude-code.sh` - One-command Claude Code + Synapse setup
- `@deploy/simple-setup.sh` - Minimal Synapse setup for existing projects
- `@deploy/sync-global.sh` - Sync project changes back to global knowledge

### Core System Scripts (neo4j/)
- `@neo4j/activate.sh` - Master system activation and health management
- `@neo4j/activate.sh --status` - Check system health
- `@neo4j/activate.sh --force` - Force re-ingestion
- `@neo4j/activate.sh --stop` - Stop all services

### Intelligence and Search Scripts (neo4j/)
- `@neo4j/context_manager.py "query"` - Intelligent hybrid search (graph + vector)
- `@neo4j/synapse_search.py "patterns"` - Agent-friendly search interface
- `@neo4j/ingestion.py --force` - Re-ingest all knowledge into graph
- `@neo4j/vector_engine.py "text"` - Generate/test BGE-M3 embeddings

### Agent Tool Interface (tools/)
- `@tools/synapse_tools.py` - Claude Code agent integration wrapper
- Provides standardized tool interfaces for agents

### Health and Diagnostics
- `@neo4j/context_manager.py --health` - System health check
- `@neo4j/context_manager.py --stale` - Check if data needs refresh
- `docker-compose ps` - Service status (run from neo4j directory)

## Integration with Claude Code Agents

Once set up, all agents can leverage Synapse intelligence:

```bash
# Context-aware development
@context-fetcher "implement authentication"

# Standards-compliant code review
@code-hound "review for SOLID principles"

# Knowledge-driven testing
@test-runner "run tests with best practices"

# Intelligent project management
@project-manager "update roadmap with progress"
```

## Expected Outcomes

1. **Intelligent Context**: Agents have access to curated development knowledge
2. **Language-Aware Guidance**: Context adapts to your chosen technology stack
3. **Pattern Recognition**: BGE-M3 embeddings enable semantic code pattern matching
4. **Continuous Learning**: System improves as it ingests your project's evolution
5. **Standards Compliance**: Built-in knowledge of best practices and conventions

This replaces traditional project setup with a knowledge-graph-powered approach that grows smarter over time.
