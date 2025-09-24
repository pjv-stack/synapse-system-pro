"""
Mock Claude Code SDK for Development

Provides mock implementations of Claude Code SDK functions for testing
and development when the actual SDK is not available.
"""

import asyncio
from typing import Any, AsyncGenerator, Callable, Dict, List, Optional, TypedDict
from dataclasses import dataclass


class ClaudeCodeSdkMessage(TypedDict):
    """Mock message structure"""
    role: str
    content: str


@dataclass
class MockServer:
    """Mock MCP server"""
    name: str
    tools: List[Callable]


def tool(func: Callable) -> Callable:
    """Mock tool decorator - just returns the function unchanged"""
    return func


def create_sdk_mcp_server(name: str, tools: List[Callable]) -> MockServer:
    """Mock MCP server creation"""
    return MockServer(name=name, tools=tools)


async def query(prompt: str, options: Optional[Dict] = None) -> AsyncGenerator[ClaudeCodeSdkMessage, None]:
    """Mock query function"""
    # Simulate a simple response
    yield ClaudeCodeSdkMessage({
        "role": "assistant",
        "content": f"Mock response to: {prompt}"
    })