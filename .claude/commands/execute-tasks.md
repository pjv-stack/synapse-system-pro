# Execute Tasks - Knowledge-Driven Implementation

Execute tasks using Synapse System intelligence for implementation guidance, pattern matching, and quality assurance.

## Pre-Execution Intelligence Gathering

### 1. System Health Verification
```bash
# Ensure Synapse system is operational
@neo4j/activate.sh --status

# Verify knowledge graph availability
@neo4j/context_manager.py --health
```

### 2. Implementation Pattern Research
```bash
# Find implementation patterns for the task
@neo4j/synapse_search.py "implementation patterns [task domain] [language]"

# Get relevant design patterns
@neo4j/synapse_search.py "design patterns [feature type]"

# Research similar implementations
@neo4j/synapse_search.py "similar implementations [task description]"
```

### 3. Standards and Best Practices Lookup
```bash
# Get coding standards for the language
@neo4j/synapse_search.py "coding standards [language]"

# Find testing strategies
@neo4j/synapse_search.py "testing strategy [component type]"

# Research error handling patterns
@neo4j/synapse_search.py "error handling [language]"
```

## Intelligent Task Execution Workflow

### 1. Context-Aware Planning
- Use `@context-fetcher` to gather relevant implementation context
- Query Synapse for similar solved problems and patterns
- Identify dependencies and prerequisites from knowledge graph

### 2. Implementation with Guidance
```bash
# Get step-by-step implementation guidance
@neo4j/synapse_search.py "step by step [feature] [language]"

# Find code templates and boilerplate
@neo4j/synapse_search.py "template [component type] [language]"

# Research integration patterns
@neo4j/synapse_search.py "integration patterns [system type]"
```

### 3. Quality Assurance Integration
```bash
# Validate against SOLID principles
@neo4j/synapse_search.py "SOLID principles [language] examples"

# Check DRY compliance patterns
@neo4j/synapse_search.py "DRY principle [language]"

# Get refactoring guidance
@neo4j/synapse_search.py "refactoring patterns [language]"
```

### 4. Testing Strategy Implementation
```bash
# Get testing patterns for the component
@neo4j/synapse_search.py "unit testing [component type] [language]"

# Find test structure patterns
@neo4j/synapse_search.py "test organization [language]"

# Research mocking and test double patterns
@neo4j/synapse_search.py "test doubles [language]"
```

## Post-Implementation Validation

### 1. Code Quality Review
```bash
# Use code-hound agent for quality enforcement
@code-hound

# Verify implementation against knowledge graph standards
@neo4j/synapse_search.py "code review checklist [language]"
```

### 2. Testing Validation
```bash
# Run tests with intelligent analysis
@test-runner

# Verify test coverage patterns
@neo4j/synapse_search.py "test coverage [language]"
```

### 3. Knowledge Graph Update
```bash
# Update project-specific knowledge base
@neo4j/ingestion.py --project-sync

# Sync learnings back to global knowledge
@deploy/sync-global.sh
```

## Integration with Other Agents

### Collaborative Execution
- **@project-manager**: Track task completion and update roadmaps
- **@context-fetcher**: Gather implementation context and patterns
- **@code-hound**: Enforce quality standards throughout implementation
- **@test-runner**: Validate implementation with comprehensive testing
- **@git-workflow**: Commit changes with knowledge-aware commit messages
- **@file-creator**: Generate files using Synapse templates

This approach ensures every task execution is informed by curated development knowledge and follows proven implementation patterns.
