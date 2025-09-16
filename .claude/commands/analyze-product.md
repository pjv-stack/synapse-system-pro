# Analyze Product - Synapse-Powered Codebase Analysis

Perform intelligent codebase analysis using Synapse System knowledge graph and vector embeddings for comprehensive product understanding.

## Synapse-Enhanced Analysis Workflow

### 1. System Setup and Health Check
```bash
# Ensure Synapse system is operational
@neo4j/activate.sh --status

# Initialize Synapse for the project
@deploy/setup-claude-code.sh --project /path/to/codebase

# Verify system health
@neo4j/context_manager.py --health
```

### 2. Language and Architecture Detection
```bash
# Automatically detect project language(s)
@deploy/init-project.sh --detect --project /path/to/codebase

# Analyze architecture patterns
@neo4j/synapse_search.py "architecture analysis [detected language]"

# Find similar project patterns
@neo4j/synapse_search.py "project structure [language] [domain]"
```

### 3. Intelligent Codebase Ingestion
```bash
# Ingest codebase into knowledge graph
cd project/.synapse
@neo4j/ingestion.py --full-analysis --project /path/to/codebase

# Generate semantic embeddings for code patterns
@neo4j/vector_engine.py --analyze-codebase /path/to/codebase
```

### 4. Comprehensive Analysis Using Knowledge Graph

#### Code Quality Assessment
```bash
# Analyze against coding standards
@neo4j/synapse_search.py "code quality patterns [language]"

# Check for architectural anti-patterns
@neo4j/synapse_search.py "architectural smells [framework]"

# Assess testing coverage patterns
@neo4j/synapse_search.py "testing completeness [language]"
```

#### Dependency and Integration Analysis
```bash
# Analyze dependency patterns
@neo4j/synapse_search.py "dependency management [language]"

# Find integration patterns
@neo4j/synapse_search.py "integration patterns [detected architecture]"

# Research security patterns
@neo4j/synapse_search.py "security analysis [framework]"
```

#### Performance and Scalability Assessment
```bash
# Research performance patterns
@neo4j/synapse_search.py "performance patterns [language] [domain]"

# Find scalability strategies
@neo4j/synapse_search.py "scalability patterns [architecture type]"

# Analyze deployment patterns
@neo4j/synapse_search.py "deployment strategies [infrastructure]"
```

### 5. Intelligent Recommendations Generation

#### Enhancement Opportunities
```bash
# Find modernization patterns
@neo4j/synapse_search.py "modernization strategies [current framework]"

# Research refactoring opportunities
@neo4j/synapse_search.py "refactoring patterns [legacy code]"

# Get optimization recommendations
@neo4j/synapse_search.py "optimization strategies [performance issue]"
```

#### Best Practices Alignment
```bash
# Compare against industry standards
@neo4j/synapse_search.py "industry best practices [domain]"

# Find compliance patterns
@neo4j/synapse_search.py "compliance requirements [industry]"

# Research maintenance strategies
@neo4j/synapse_search.py "maintenance patterns [system age]"
```

### 6. Project-Specific Knowledge Base Creation
```bash
# Create project-specific documentation
@neo4j/synapse_search.py "documentation templates [project type]"

# Generate architectural decision records
@neo4j/synapse_search.py "ADR templates [technology stack]"

# Create development guidelines
@neo4j/synapse_search.py "development guidelines [team size]"
```

## Analysis Report Generation

### Executive Summary
- **Technology Stack Assessment**: Compare against modern alternatives
- **Architecture Quality**: Evaluate against known patterns
- **Technical Debt Analysis**: Identify areas needing attention
- **Security Posture**: Assess against security best practices

### Technical Recommendations
- **Immediate Improvements**: Quick wins from knowledge graph patterns
- **Strategic Enhancements**: Long-term architectural improvements
- **Tooling Upgrades**: Development environment optimizations
- **Process Improvements**: Workflow and methodology enhancements

### Implementation Roadmap
- **Phase 1**: Critical issues and quick improvements
- **Phase 2**: Strategic architectural changes
- **Phase 3**: Advanced optimizations and modern practices

This approach leverages the full power of the Synapse knowledge graph to provide insights that go beyond basic static analysis, incorporating industry best practices and proven patterns.
