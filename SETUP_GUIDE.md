# Synapse Setup Guide for Beginners

*A simple, step-by-step guide to set up and use Synapse in your projects*

## 1.) what

Imagine giving your AI assistant a memory system that remembers:
- Your project's coding patterns
- Your preferred libraries and frameworks
- Your team's conventions and standards
- Past solutions to similar problems

That's what Synapse does! It creates a "knowledge base" that travels with your project.

## 🚀 Quick Start Workflow

```
1. Set Up Synapse Globally (one time)
   ↓
2. Copy Synapse to Your Project
   ↓
3. Let the Agent Configure Everything
   ↓
4. Start Coding with Context-Aware AI!
```

---

## Part 1: Global Setup (Do This Once)

### Step 1: Check Your Prerequisites

Open a terminal and check:

```bash
# Check Python version (need 3.12+)
python3 --version
# Should show: Python 3.12.x or higher

# Check if Docker is running
docker --version
# Should show: Docker version xx.x.x

# Check if uv is installed
uv --version
# If not installed, run this:
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Step 2: Start Synapse Services

Run the magic command:

```bash
~/.synapse-system/synapse start
```

**What happens:**
- 🐳 Starts Docker containers (Neo4j database + Redis cache)
- 🧠 Downloads BGE-M3 model (2.3GB - only first time)
- 📚 Builds the global knowledge base
- ✅ Runs health checks

**Expected output:**
```
[SYNAPSE] Checking environment setup...
✓ Environment validated
[SYNAPSE] Starting services...
✓ Neo4j started
✓ Redis started
[SYNAPSE] Building knowledge base...
Loading BGE-M3 model: BAAI/bge-m3
BGE-M3 model loaded successfully.
✓ Ingestion complete: 47 files processed
[SYNAPSE] System ready!
```

**⏱️ First run takes ~10 minutes (downloads + setup)**
**⏱️ Future runs take ~1 minute**

---

## Part 2: Setting Up a New Project

Let's walk through setting up a Rust project called `my-awesome-app`:

### Step 1: Navigate to Your Project

```bash
cd /path/to/your/project
# Example: cd ~/dev/my-awesome-app
```

### Step 2: Initialize Your Project

```bash
~/.synapse-system/synapse init .
```

This automatically detects your project language and creates the appropriate setup:

```
my-awesome-app/
├── src/
├── Cargo.toml          # Rust project file (detected)
├── README.md
├── .synapse/           # ← Your project's knowledge base
│   ├── instructions/   # Rust-specific guides
│   ├── standards/      # Rust conventions
│   └── templates/      # Rust patterns
├── .claude/            # ← Claude Code integration
│   └── agents/         # Language-specific agents
└── .synapse.yml        # Configuration
```

### Step 3: Start Using with Claude Code

Your project is now ready! Simply use:

```
@synapse-project-manager

Help me implement authentication following Rust best practices.
```

**The agent now has:**
- 🔍 **Language awareness**: Knows this is a Rust project
- ⚙️ **Rust-specific knowledge**: Error handling patterns, testing conventions, naming standards
- 🧠 **Project context**: Understanding of your specific codebase structure
- 📚 **Best practices**: Curated Rust development patterns
- 🔧 **Search capabilities**: Can query both global and project-specific knowledge

---

## Part 3: Using Synapse Day-to-Day

### Scenario: Adding Authentication to Your App

**You want to add JWT authentication. Here's how Synapse helps:**

#### Option 1: Ask Claude for Help

```
Hey Claude, I need to add JWT authentication to my Rust API.
Can you help me implement this following our project's patterns?
```

**Claude (with Synapse) responds:**
- 🔍 Searches your existing auth patterns
- 📖 References Rust JWT best practices
- 🎯 Checks your error handling conventions
- ✅ Provides code that fits your style

#### Option 2: Search Knowledge Directly

```bash
# Search global knowledge base
~/.synapse-system/synapse search "rust authentication patterns"
~/.synapse-system/synapse search "error handling best practices"
~/.synapse-system/synapse search "database connection patterns"
```

### Scenario: Working on Error Handling

Instead of googling "Rust error handling", you can:

```bash
~/.synapse-system/synapse search "rust error handling best practices"
```

**Results include:**
- Your project's current error patterns
- Rust-specific error handling standards
- Examples from your existing code
- Related patterns and conventions

---

## Part 4: Real Examples

### Example 1: Rust Web API Project

```bash
# Your project structure
my-rust-api/
├── src/
│   ├── main.rs
│   ├── handlers/
│   └── models/
├── Cargo.toml
└── .synapse/

# After agent setup, ask Claude:
"Help me add a new user registration endpoint"

# Claude knows:
✓ Your existing handler patterns
✓ Your database models
✓ Your error handling approach
✓ Your testing conventions
```

### Example 2: TypeScript React Project

```bash
# Your project structure
my-react-app/
├── src/
│   ├── components/
│   └── hooks/
├── package.json
└── .synapse/

# After agent setup, ask Claude:
"Create a new user profile component"

# Claude knows:
✓ Your component structure patterns
✓ Your TypeScript interfaces
✓ Your styling approach (CSS modules, styled-components, etc.)
✓ Your testing setup
```

---

## 🛠️ Troubleshooting

### "Services not starting"

```bash
# Check Docker is running
sudo systemctl status docker

# Restart Docker if needed
sudo systemctl start docker

# Try starting synapse again
~/.synapse-system/synapse start
```

### "BGE-M3 model not downloading"

```bash
# Check internet connection
ping huggingface.co

# Check disk space (need ~3GB free)
df -h

# Manually test the model
cd ~/.synapse-system/neo4j
python vector_engine.py "test"
```

### "Agent not finding my project files"

```bash
# Make sure you're in the right directory
pwd
ls -la  # Should see .synapse/ and .claude/ folders

# Re-initialize project if needed
~/.synapse-system/synapse init . --force
```

### "Search not returning results"

```bash
# Check system status
~/.synapse-system/synapse status

# Start services if needed
~/.synapse-system/synapse start

# Test search functionality
~/.synapse-system/synapse search "test query"
```

---

## 🎯 Quick Reference

### Global Commands
```bash
# Start Synapse system
~/.synapse-system/synapse start

# Check system status
~/.synapse-system/synapse status

# Stop all services
~/.synapse-system/synapse stop
```

### Project Setup Commands
```bash
# Initialize project with synapse
~/.synapse-system/synapse init .

# Then use agents in Claude Code:
# @synapse-project-manager
# @rust-specialist (or other language specialist)
```

### Daily Usage Commands
```bash
# Search global knowledge base
~/.synapse-system/synapse search "your query here"

# Get help
~/.synapse-system/synapse help

# Check system health
~/.synapse-system/synapse status
```

---

## 🧭 What's Next?

After setup, every time you work with Claude Code:

1. **Claude remembers your patterns** - No more explaining your conventions
2. **Suggestions match your style** - Code fits seamlessly into your project
3. **Context-aware responses** - Claude knows your existing architecture
4. **Faster development** - Less time explaining, more time building

### Advanced Usage

Once comfortable, explore:
- Multiple language projects (Rust backend + TypeScript frontend)
- Custom templates for your team
- Integration with CI/CD pipelines
- Sharing knowledge bases across team projects

---

## 📚 Visual Workflow Summary

```
GLOBAL SETUP (One Time)
┌─────────────────────────────┐
│ ~/.synapse-system/          │
│ ├── Global Knowledge Base   │
│ ├── Standards & Templates   │
│ └── BGE-M3 Model           │
└─────────────────────────────┘
              │
              ▼
         [activate.sh]
              │
              ▼
    ┌─────────────────┐
    │ Services Ready  │
    │ ✓ Neo4j         │
    │ ✓ Redis         │
    │ ✓ BGE-M3        │
    └─────────────────┘

PROJECT SETUP (Per Project)
┌─────────────────┐     ┌─────────────────────┐
│ Your Project    │────▶│ cp -r ~/.synapse    │
│ └── src/        │     │       .synapse      │
│ └── Cargo.toml  │     └─────────────────────┘
└─────────────────┘                │
                                   ▼
            ┌──────────────────────────────────┐
            │ @synapse-project-manager         │
            │ "Set up synapse for my project"  │
            └──────────────────────────────────┘
                           │
                           ▼
               ┌─────────────────────┐
               │ Project Brain Ready │
               │ ✓ Language detected │
               │ ✓ Templates set up  │
               │ ✓ Knowledge ingested│
               │ ✓ Embeddings ready  │
               └─────────────────────┘

DAILY USAGE
┌─────────────────┐     ┌─────────────────┐
│ Ask Claude      │────▶│ Context-Aware   │
│ "Add feature X" │     │ Response        │
└─────────────────┘     │ ✓ Matches style │
                        │ ✓ Uses patterns │
                        │ ✓ Fits project  │
                        └─────────────────┘
```

You're now ready to build with AI that remembers everything about your project! 🚀
