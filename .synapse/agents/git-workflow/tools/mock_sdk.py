"""
Mock Claude Code SDK for Git Workflow

Development fallback when actual SDK is not available.
"""

import asyncio
from typing import Any, AsyncGenerator, Dict, List, Optional, Callable
from dataclasses import dataclass

# Type definitions matching real SDK
ClaudeCodeSdkMessage = Dict[str, Any]

@dataclass
class MockTool:
    """Mock tool registration."""
    name: str
    func: Callable
    description: str = ""

class MockMCPServer:
    """Mock MCP Server for git workflow development."""

    def __init__(self, name: str, tools: List[MockTool]):
        self.name = name
        self.tools = {tool.name: tool for tool in tools}
        self.running = False

    async def run(self):
        """Mock server run method."""
        self.running = True
        print(f"🌿 Mock Git Workflow Server '{self.name}' started with {len(self.tools)} tools")

    async def stop(self):
        """Mock server stop method."""
        self.running = False
        print(f"🌿 Mock Git Workflow Server '{self.name}' stopped")

def create_sdk_mcp_server(name: str, tools: List[Callable]) -> MockMCPServer:
    """Create a mock MCP server with git workflow tools."""
    mock_tools = []
    for tool_func in tools:
        tool_name = tool_func.__name__
        tool_desc = tool_func.__doc__ or "Git workflow tool"
        mock_tools.append(MockTool(name=tool_name, func=tool_func, description=tool_desc))

    return MockMCPServer(name, mock_tools)

def tool(func: Callable) -> Callable:
    """Mock tool decorator for git workflow functions."""
    func._is_tool = True
    func._tool_name = func.__name__
    func._tool_description = func.__doc__ or "Git workflow operation"

    def wrapper(*args, **kwargs):
        print(f"🌿 Mock git tool '{func.__name__}' called")
        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    wrapper._is_tool = True
    wrapper._tool_name = func._tool_name
    wrapper._tool_description = func._tool_description

    return wrapper

async def query(prompt: str, options: Optional[Dict[str, Any]] = None) -> AsyncGenerator[ClaudeCodeSdkMessage, None]:
    """Mock query function for git workflow operations."""
    print(f"🌿 Mock git workflow query: {prompt[:30]}{'...' if len(prompt) > 30 else ''}")

    await asyncio.sleep(0.1)

    mock_responses = [
        {
            "type": "message",
            "content": "Hello! I'm Git Workflow Agent, ready to handle version control operations.",
            "metadata": {"source": "mock_sdk"}
        },
        {
            "type": "tool_request",
            "tool": "execute_complete_workflow",
            "args": {"action": "feature", "target_branch": "main"},
            "metadata": {"source": "mock_sdk"}
        }
    ]

    for response in mock_responses:
        yield response
        await asyncio.sleep(0.05)