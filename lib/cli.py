#!/usr/bin/env python3
"""
Synapse System - Unified CLI
============================

Single entry point for all synapse functionality with intelligent context detection.
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path
from typing import Optional, Dict, List, Any

# Add current directory to path for local imports
sys.path.insert(0, os.path.dirname(__file__))

from project import ProjectManager
from updater import UpdateManager
from version_manager import VersionManager


class SynapseCLI:
    """Unified command-line interface for Synapse System"""

    def __init__(self):
        self.synapse_home = Path(__file__).parent.parent.resolve()
        self.neo4j_dir = self.synapse_home / ".synapse" / "neo4j"
        self.project_manager = ProjectManager(self.synapse_home)
        self.update_manager = UpdateManager(self.synapse_home)
        self.version_manager = VersionManager(self.synapse_home)

        # Auto-detect current project context
        self.current_project = self._find_project_root()

    def _find_project_root(self) -> Optional[Path]:
        """Find synapse project by walking up directories"""
        current = Path.cwd()
        while current.parent != current:
            if (current / ".synapse.yml").exists():
                return current
            current = current.parent
        return None

    def _run_neo4j_script(self, script_name: str, args: List[str] = None) -> int:
        """Run a script in the Neo4j environment"""
        if args is None:
            args = []

        venv_python = self.neo4j_dir / ".venv" / "bin" / "python"
        script_path = self.neo4j_dir / script_name

        if not script_path.exists():
            print(f"Error: Script {script_name} not found", file=sys.stderr)
            return 1

        try:
            result = subprocess.run(
                [str(venv_python), str(script_path)] + args,
                cwd=self.neo4j_dir
            )
            return result.returncode
        except Exception as e:
            print(f"Error running {script_name}: {e}", file=sys.stderr)
            return 1

    def _check_services(self) -> bool:
        """Quick check if synapse services are running"""
        try:
            import requests
            response = requests.get("http://localhost:7474", timeout=2)
            return response.status_code == 200
        except:
            return False

    def cmd_start(self, args) -> int:
        """Start synapse services"""
        print("🚀 Starting synapse services...")

        # Check if Docker is available
        try:
            subprocess.run(["docker", "--version"],
                         capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Docker is required but not installed")
            return 1

        # Start services via docker-compose
        try:
            result = subprocess.run(
                ["docker-compose", "up", "-d"],
                cwd=self.neo4j_dir,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                print("✅ Synapse services started successfully")
                print("🔗 Neo4j: http://localhost:7474")
                print("🔗 Redis: localhost:6379")
                return 0
            else:
                print(f"❌ Failed to start services: {result.stderr}")
                return 1

        except Exception as e:
            print(f"❌ Error starting services: {e}")
            return 1

    def cmd_stop(self, args) -> int:
        """Stop synapse services"""
        print("🛑 Stopping synapse services...")

        try:
            result = subprocess.run(
                ["docker-compose", "down"],
                cwd=self.neo4j_dir,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                print("✅ Synapse services stopped")
                return 0
            else:
                print(f"❌ Failed to stop services: {result.stderr}")
                return 1

        except Exception as e:
            print(f"❌ Error stopping services: {e}")
            return 1

    def cmd_status(self, args) -> int:
        """Check synapse system status"""
        print("📊 Synapse System Status")
        print("=" * 30)

        # Check services
        print("\n🔧 Services:")
        if self._check_services():
            print("✅ Neo4j running on http://localhost:7474")
        else:
            print("❌ Neo4j not responding")

        # Check Redis
        try:
            import redis
            r = redis.Redis(host='localhost', port=6379, socket_timeout=2)
            r.ping()
            print("✅ Redis running on localhost:6379")
        except:
            print("❌ Redis not responding")

        # Project context
        print(f"\n📁 Current Directory: {Path.cwd()}")
        if self.current_project:
            print(f"✅ Synapse project detected: {self.current_project}")
            config = self.project_manager.load_project_config(self.current_project)
            if config:
                print(f"   Language: {config.get('language', 'unknown')}")
                print(f"   Version: {config.get('synapse_version', 'unknown')}")
        else:
            print("ℹ️  No synapse project in current directory")

        return 0

    def cmd_search(self, args) -> int:
        """Search global knowledge base"""
        if not args.query:
            print("❌ Search query required")
            print("Usage: synapse search \"your query\"")
            return 1

        if not self._check_services():
            print("⚠️  Services not running, starting them...")
            if self.cmd_start(None) != 0:
                return 1
            import time
            time.sleep(2)

        print(f"🔍 Searching for: {args.query}")
        return self._run_neo4j_script("synapse_search.py", [args.query])

    def cmd_init(self, args) -> int:
        """Initialize project with synapse"""
        target_dir = Path(args.directory) if args.directory else Path.cwd()

        if not target_dir.exists():
            print(f"❌ Directory does not exist: {target_dir}")
            return 1

        if not target_dir.is_dir():
            print(f"❌ Not a directory: {target_dir}")
            return 1

        print(f"🎯 Initializing synapse for: {target_dir.name}")

        try:
            self.project_manager.initialize_project(
                target_dir,
                link_agents=args.link if hasattr(args, 'link') else False
            )
            print("✅ Project initialized successfully!")
            return 0
        except Exception as e:
            print(f"❌ Initialization failed: {e}")
            return 1

    def cmd_update(self, args) -> int:
        """Update project agents and configuration"""
        target_dir = Path(args.directory) if args.directory else self.current_project

        if not target_dir:
            print("❌ No synapse project found in current directory")
            print("Use: synapse update /path/to/project")
            return 1

        if not (target_dir / ".synapse.yml").exists():
            print(f"❌ Not a synapse project: {target_dir}")
            return 1

        print(f"🔄 Updating synapse project: {target_dir.name}")

        try:
            updates = self.update_manager.check_updates(target_dir)
            if not updates:
                print("✅ Project is up to date")
                return 0

            print(f"📦 Found {len(updates)} updates:")
            for update in updates:
                print(f"   • {update['name']}: {update['old_version']} → {update['new_version']}")

            if not args.yes:
                response = input("\nApply updates? [y/N]: ")
                if response.lower() not in ['y', 'yes']:
                    print("Update cancelled")
                    return 0

            self.update_manager.apply_updates(target_dir, updates)
            print("✅ Project updated successfully!")
            return 0

        except Exception as e:
            print(f"❌ Update failed: {e}")
            return 1

    def cmd_ingest(self, args) -> int:
        """Ingest knowledge into synapse"""
        if self.current_project:
            print(f"📚 Ingesting project: {self.current_project.name}")
        else:
            print("📚 Ingesting global knowledge")

        script_args = []
        if args.force:
            script_args.append("--force")

        return self._run_neo4j_script("ingestion.py", script_args)

    def cmd_health(self, args) -> int:
        """Check system health"""
        if self.current_project:
            print(f"🩺 Health check for project: {self.current_project.name}")
        else:
            print("🩺 Global system health check")

        return self._run_neo4j_script("synapse_health.py")

    def cmd_standards(self, args) -> int:
        """Get coding standards"""
        if not args.name:
            print("❌ Standard name required")
            print("Usage: synapse standards <name> [language]")
            return 1

        script_args = [args.name]
        if args.language:
            script_args.append(args.language)
        elif self.current_project:
            # Auto-detect language from project
            config = self.project_manager.load_project_config(self.current_project)
            if config and config.get('language'):
                script_args.append(config['language'])

        return self._run_neo4j_script("synapse_standard.py", script_args)

    def cmd_template(self, args) -> int:
        """Get project templates"""
        if not args.name:
            print("❌ Template name required")
            print("Usage: synapse template <name>")
            return 1

        return self._run_neo4j_script("synapse_template.py", [args.name])

    def cmd_tool(self, args) -> int:
        """Direct tool access (for debugging)"""
        tool_map = {
            'search': ('synapse_search.py', ['query']),
            'standard': ('synapse_standard.py', ['name', 'language']),
            'template': ('synapse_template.py', ['name']),
            'health': ('synapse_health.py', []),
        }

        if args.tool_name not in tool_map:
            print(f"❌ Unknown tool: {args.tool_name}")
            print(f"Available tools: {', '.join(tool_map.keys())}")
            return 1

        script_name, param_names = tool_map[args.tool_name]
        script_args = args.tool_args if args.tool_args else []

        return self._run_neo4j_script(script_name, script_args)

    def cmd_version(self, args) -> int:
        """Show version information"""
        version_file = self.synapse_home / ".synapse" / "VERSION"
        if version_file.exists():
            version = version_file.read_text().strip()
        else:
            version = "unknown"

        print(f"Synapse System v{version}")
        print(f"Location: {self.synapse_home}")

        if self.current_project:
            config = self.project_manager.load_project_config(self.current_project)
            if config:
                proj_version = config.get('synapse_version', 'unknown')
                print(f"Project version: {proj_version}")
                if proj_version != version:
                    print("⚠️  Project version differs from system version")
                    print("   Consider running: synapse update")

        return 0

    def cmd_manifest(self, args) -> int:
        """Manage agent manifest and versions"""
        if args.manifest_action == "update":
            try:
                self.version_manager.update_manifest()
                return 0
            except Exception as e:
                print(f"❌ Failed to update manifest: {e}")
                return 1

        elif args.manifest_action == "verify":
            if args.agent:
                success = self.version_manager.verify_agent_integrity(args.agent)
                return 0 if success else 1
            else:
                success = self.version_manager.verify_all_agents()
                return 0 if success else 1

        elif args.manifest_action == "list":
            self.version_manager.list_agents_summary()
            return 0

        elif args.manifest_action == "info":
            if not args.agent:
                print("❌ Agent name required for info command")
                return 1
            info = self.version_manager.get_agent_info(args.agent)
            if "error" in info:
                print(f"❌ {info['error']}")
                return 1

            import json
            print(json.dumps(info, indent=2))
            return 0

        else:
            print(f"❌ Unknown manifest action: {args.manifest_action}")
            return 1


def main():
    """Main CLI entry point"""
    cli = SynapseCLI()

    parser = argparse.ArgumentParser(
        description="Synapse System - Global Knowledge and Agent Management",
        prog="synapse"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Service management
    subparsers.add_parser("start", help="Start synapse services")
    subparsers.add_parser("stop", help="Stop synapse services")
    subparsers.add_parser("status", help="Check system status")

    # Core functionality
    search_parser = subparsers.add_parser("search", help="Search global knowledge")
    search_parser.add_argument("query", help="Search query")

    init_parser = subparsers.add_parser("init", help="Initialize project")
    init_parser.add_argument("directory", nargs="?", help="Project directory")
    init_parser.add_argument("--link", action="store_true",
                           help="Use symlinks instead of copies")

    update_parser = subparsers.add_parser("update", help="Update project")
    update_parser.add_argument("directory", nargs="?", help="Project directory")
    update_parser.add_argument("-y", "--yes", action="store_true",
                             help="Apply updates without confirmation")

    # Knowledge management
    ingest_parser = subparsers.add_parser("ingest", help="Ingest knowledge")
    ingest_parser.add_argument("--force", action="store_true",
                             help="Force full re-ingestion")

    subparsers.add_parser("health", help="System health check")

    # Content access
    standards_parser = subparsers.add_parser("standards", help="Get coding standards")
    standards_parser.add_argument("name", help="Standard name")
    standards_parser.add_argument("language", nargs="?", help="Programming language")

    template_parser = subparsers.add_parser("template", help="Get templates")
    template_parser.add_argument("name", help="Template name")

    # Tool access
    tool_parser = subparsers.add_parser("tool", help="Direct tool access")
    tool_parser.add_argument("tool_name", choices=["search", "standard", "template", "health"])
    tool_parser.add_argument("tool_args", nargs="*", help="Tool arguments")

    # Utility
    subparsers.add_parser("version", help="Show version information")

    # Manifest management
    manifest_parser = subparsers.add_parser("manifest", help="Manage agent manifest")
    manifest_parser.add_argument("manifest_action", choices=["update", "verify", "list", "info"])
    manifest_parser.add_argument("agent", nargs="?", help="Agent name (for verify/info)")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Route to appropriate command handler
    cmd_method = getattr(cli, f"cmd_{args.command.replace('-', '_')}", None)
    if cmd_method:
        return cmd_method(args)
    else:
        print(f"❌ Unknown command: {args.command}")
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())