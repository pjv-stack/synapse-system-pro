# Synapse Setup Guide

Give your AI assistant memory of your coding patterns and project conventions.

## One-Command Setup

```bash
git clone https://github.com/your-repo/synapse-system.git ~/.synapse-system
cd ~/.synapse-system && ./install.sh
```

**That's it!** The installer handles everything automatically:
- ✅ Checks prerequisites (fixes what it can)
- ✅ Installs dependencies
- ✅ Starts services (Neo4j + Redis)
- ✅ Downloads AI model (~2.3GB first time)
- ✅ Runs health checks

**First install takes ~5 minutes.** Future startups are instant.

**Having issues?** Run `synapse doctor --fix` to auto-resolve problems.

## Project Setup

```bash
# In any project directory
cd my-project/
synapse init .
```

**What happens:**
- 🔍 Auto-detects your language (Rust, TypeScript, Go, Python)
- 📁 Creates `.claude/agents/` with specialized AI agents
- ⚙️ Sets up `.synapse.yml` configuration
- ✅ Ready for Claude Code!

**Now use with Claude Code:**
```
@synapse-project-manager help me implement authentication
@rust-specialist write error handling following our patterns
```

## Daily Usage

**Instead of explaining your patterns every time:**

```
@synapse-project-manager I need JWT authentication for this API
```

**Synapse knows:**
- ✅ Your existing patterns and conventions
- ✅ Your error handling approach
- ✅ Your testing standards
- ✅ Language-specific best practices

**Search for patterns:**
```bash
synapse search "rust error handling"
synapse search "async patterns"
```

## Troubleshooting

**Most issues fix themselves:**
```bash
synapse doctor --fix
```

**Common fixes:**
- **Docker not running:** `sudo systemctl start docker`
- **Services not starting:** `synapse stop && synapse start`
- **Search not working:** Check `synapse status`

## You're Ready!

Now Claude remembers your patterns, conventions, and codebase structure. No more explaining the same things over and over! 🚀
