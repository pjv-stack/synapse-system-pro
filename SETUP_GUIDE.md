# Synapse Setup Guide for Beginners

*A simple, step-by-step guide to set up and use Synapse in your projects*

## 🎯 What You're Building

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
~/.synapse-system/neo4j/activate.sh
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

### Step 2: Copy Synapse Into Your Project

```bash
cp -r ~/.synapse-system .synapse
```

This creates a `.synapse/` folder in your project. Think of it as your project's "brain"!

```
my-awesome-app/
├── src/
├── Cargo.toml          # Rust project file
├── README.md
└── .synapse/           # ← Your project's knowledge base
    ├── instructions/
    ├── templates/
    ├── vector_engine.py
    └── ...
```

### Step 3: Let the Agent Set Everything Up

Open **Claude Code** and type:

```
@synapse-project-manager

I just copied synapse into my project. Please set it up - detect the language, configure the templates, and initialize the knowledge base.
```

**The agent will:**
1. 🔍 **Detect your language**: "I see Cargo.toml - this is a Rust project!"
2. ⚙️ **Configure Rust-specific templates**: Error handling patterns, testing conventions
3. 🧠 **Set up BGE-M3 embeddings**: Creates semantic understanding of your code
4. 📚 **Build project knowledge base**: Ingests your README, docs, config files
5. 🔧 **Create search tools**: So you can query your project's context

**Expected conversation:**
```
Agent: I've detected this is a Rust project based on Cargo.toml. Let me configure Synapse for Rust development.

✓ Language detected: Rust
✓ Copied Rust-specific templates and standards
✓ Initialized BGE-M3 embeddings (1024-dimensional vectors)
✓ Ingested project files: Cargo.toml, README.md, src/
✓ Created project search capabilities

Your Synapse setup is complete! I can now help with Rust-specific development using your project's context.
```

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

#### Option 2: Search Your Project Directly

```bash
cd .synapse
python search.py "authentication patterns"
python search.py "error handling in our API"
python search.py "how do we handle database connections"
```

### Scenario: Working on Error Handling

Instead of googling "Rust error handling", you can:

```bash
cd .synapse
python search.py "error handling best practices"
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

# Try activation again
~/.synapse-system/neo4j/activate.sh
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
ls -la  # Should see .synapse/ folder

# Re-run ingestion manually
cd .synapse
python ingest.py --force
```

### "Search not returning results"

```bash
# Check if knowledge base was built
cd .synapse
python search.py --help

# Rebuild the knowledge base
python ingest.py --force
```

---

## 🎯 Quick Reference

### Global Commands
```bash
# Start Synapse system
~/.synapse-system/neo4j/activate.sh

# Check system status
~/.synapse-system/neo4j/activate.sh --status

# Stop all services
~/.synapse-system/neo4j/activate.sh --stop
```

### Project Setup Commands
```bash
# Copy Synapse to project
cp -r ~/.synapse-system .synapse

# Then use @synapse-project-manager agent in Claude Code
```

### Daily Usage Commands
```bash
# Search your project's knowledge
cd .synapse
python search.py "your query here"

# Update knowledge base after big changes
python ingest.py

# Test BGE-M3 embeddings
python vector_engine.py "test text"
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