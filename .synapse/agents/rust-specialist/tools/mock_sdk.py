"""
Mock Claude Code SDK Implementation

Provides fallback implementations for development and testing
when the Claude Code SDK is not available.
"""

import asyncio
from typing import Any, AsyncGenerator, Dict, List, Optional
from dataclasses import dataclass


@dataclass
class ClaudeCodeSdkMessage:
    """Mock message structure."""
    content: str
    type: str = "text"


class MockMCPServer:
    """Mock MCP server implementation."""

    def __init__(self, name: str):
        self.name = name
        self.tools = []

    def add_tool(self, tool_func):
        """Add a tool to the mock server."""
        self.tools.append(tool_func)


def create_sdk_mcp_server(name: str) -> MockMCPServer:
    """Create a mock MCP server."""
    print(f"🔧 Mock MCP Server created: {name}")
    return MockMCPServer(name)


def tool(func):
    """Mock tool decorator."""
    def wrapper(*args, **kwargs):
        print(f"🔧 Mock tool called: {func.__name__}")
        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


async def query(prompt: str, options: Optional[Dict[str, Any]] = None) -> AsyncGenerator[ClaudeCodeSdkMessage, None]:
    """Mock query function."""
    print(f"🤖 Mock query received: {prompt[:100]}...")

    # Simulate a response
    await asyncio.sleep(0.1)  # Simulate processing time

    response = f"Mock response to Rust specialist query. This is a development fallback."
    yield ClaudeCodeSdkMessage(content=response)

    # Keep the mock server running
    while True:
        await asyncio.sleep(1)
        user_input = "Mock user input for development testing"
        yield ClaudeCodeSdkMessage(content=user_input)