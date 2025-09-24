#!/usr/bin/env python3
"""
File Creator Agent: Intelligent File and Directory Creation

Handles template-driven file creation with Synapse System integration.
Implements the standard agent pattern with @tool decorators.
"""

import asyncio
import sys
from pathlib import Path
from typing import Any, AsyncGenerator, TypedDict

# Add tools to path
sys.path.insert(0, str(Path(__file__).parent))

# Claude Code SDK imports (placeholders for now)
try:
    from claude_code_sdk import (
        create_sdk_mcp_server,
        tool,
        query,
        ClaudeCodeSdkMessage
    )
except ImportError:
    # Fallback for development/testing
    print("⚠️  Claude Code SDK not available, using mock implementations")
    from tools.mock_sdk import (
        create_sdk_mcp_server,
        tool,
        query,
        ClaudeCodeSdkMessage
    )

from tools import (
    create_file, create_directory, batch_create,
    apply_template, get_template, list_templates,
    query_synapse_templates, search_file_patterns
)

from rich.console import Console
from rich.panel import Panel

console = Console()

# Tool argument schemas
class CreateFileArgs(TypedDict):
    file_path: str
    content: str
    template_name: str

class CreateDirectoryArgs(TypedDict):
    dir_path: str
    structure: dict

class BatchCreateArgs(TypedDict):
    file_list: list

class TemplateArgs(TypedDict):
    template_name: str
    variables: dict

class SearchArgs(TypedDict):
    query: str


# Agent tools with decorators
@tool
async def create_single_file(args: CreateFileArgs) -> dict[str, Any]:
    """Create a single file with optional template processing."""
    return await create_file(
        args["file_path"],
        args.get("content", ""),
        args.get("template_name")
    )


@tool
async def create_directory_structure(args: CreateDirectoryArgs) -> dict[str, Any]:
    """Create directory with optional nested structure."""
    return await create_directory(
        args["dir_path"],
        args.get("structure")
    )


@tool
async def batch_create_files(args: BatchCreateArgs) -> dict[str, Any]:
    """Create multiple files in a batch operation."""
    return await batch_create(args["file_list"])


@tool
async def apply_file_template(args: TemplateArgs) -> dict[str, Any]:
    """Apply a template with variable substitution."""
    return await apply_template(
        args["template_name"],
        args.get("variables", {})
    )


@tool
async def get_template_content(args: TemplateArgs) -> dict[str, Any]:
    """Retrieve template content by name."""
    return await get_template(args["template_name"])


@tool
async def list_available_templates(args: dict) -> dict[str, Any]:
    """List all available templates."""
    return await list_templates()


@tool
async def search_templates(args: SearchArgs) -> dict[str, Any]:
    """Search for templates in Synapse knowledge graph."""
    return await query_synapse_templates(args["query"])


@tool
async def search_file_structure_patterns(args: SearchArgs) -> dict[str, Any]:
    """Search for file structure patterns."""
    return await search_file_patterns(args["query"])


async def main():
    """Main agent entry point."""
    try:
        # Load configuration
        agent_dir = Path(__file__).parent

        console.print(Panel(
            "[bold green]File Creator Agent[/bold green]\n"
            "Template-driven file and directory creation\n"
            "Connected to Synapse System for intelligent templates",
            title="🗂️  Agent Ready"
        ))

        # Create MCP server with tools
        server = create_sdk_mcp_server(
            name="file_creator_tools",
            tools=[
                create_single_file,
                create_directory_structure,
                batch_create_files,
                apply_file_template,
                get_template_content,
                list_available_templates,
                search_templates,
                search_file_structure_patterns
            ]
        )

        console.print(f"[green]✓[/green] MCP Server created with {len(server.tools)} tools")

        # Load system prompt
        prompt_file = agent_dir / "file_creator_prompt.md"
        if prompt_file.exists():
            system_prompt = prompt_file.read_text()
            console.print("[green]✓[/green] System prompt loaded")
        else:
            system_prompt = "You are a file creation agent."
            console.print("[yellow]⚠[/yellow] Using default prompt")

        # Agent loop - in real implementation, this would handle incoming requests
        console.print("[cyan]Agent ready for @file-creator calls[/cyan]")

        # For now, just demonstrate the tools are available
        await demo_tools()

    except KeyboardInterrupt:
        console.print("\n[yellow]Agent shutdown requested[/yellow]")
    except Exception as e:
        console.print(f"[red]Agent error: {e}[/red]")


async def demo_tools():
    """Demonstrate available tools."""
    console.print("\n[bold]Available Tools:[/bold]")

    tools_demo = [
        "create_single_file - Create individual files with templates",
        "create_directory_structure - Create directory hierarchies",
        "batch_create_files - Create multiple files efficiently",
        "apply_file_template - Process templates with variables",
        "get_template_content - Retrieve template content",
        "list_available_templates - Show all available templates",
        "search_templates - Find templates in Synapse",
        "search_file_structure_patterns - Find file patterns"
    ]

    for tool_desc in tools_demo:
        console.print(f"  [green]•[/green] {tool_desc}")


if __name__ == "__main__":
    asyncio.run(main())