"""
Mock Claude Code SDK implementation for development and testing.
Provides the same interface as the real SDK for agent development.
"""

import asyncio
import json
from typing import Any, AsyncGenerator, Dict, List, Optional, TypedDict
from dataclasses import dataclass


@dataclass
class ClaudeCodeSdkMessage:
    """Message structure for Claude Code SDK communication."""
    role: str
    content: str
    metadata: Optional[Dict[str, Any]] = None


class MockMCPServer:
    """Mock MCP Server for development."""

    def __init__(self, name: str, tools: List[Any]):
        self.name = name
        self.tools = tools
        print(f"🔧 Mock MCP Server '{name}' initialized with {len(tools)} tools")

    async def run(self):
        """Run the mock server."""
        print(f"🚀 Mock MCP Server '{self.name}' running...")

        # Keep the server running
        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            print(f"🛑 Mock MCP Server '{self.name}' shutting down...")


def create_sdk_mcp_server(name: str, tools: List[Any]) -> MockMCPServer:
    """
    Create a mock MCP server with the given tools.

    Args:
        name: Server name
        tools: List of tool functions

    Returns:
        MockMCPServer instance
    """
    return MockMCPServer(name, tools)


def tool(func):
    """
    Mock tool decorator that preserves function metadata.

    Args:
        func: Function to decorate as a tool

    Returns:
        Decorated function with tool metadata
    """
    func._is_tool = True
    func._tool_name = func.__name__
    func._tool_description = func.__doc__ or f"Tool: {func.__name__}"

    print(f"🔨 Registered tool: {func.__name__}")

    return func


async def query(prompt: str, options: Dict[str, Any] = None) -> AsyncGenerator[ClaudeCodeSdkMessage, None]:
    """
    Mock query function that simulates Claude Code SDK responses.

    Args:
        prompt: Query prompt
        options: Query options

    Yields:
        ClaudeCodeSdkMessage responses
    """
    if options is None:
        options = {}

    print(f"💭 Mock query received: {prompt[:100]}{'...' if len(prompt) > 100 else ''}")

    # Simulate a response
    response = f"Mock response to: {prompt[:50]}{'...' if len(prompt) > 50 else ''}"

    yield ClaudeCodeSdkMessage(
        role="assistant",
        content=response,
        metadata={"mock": True, "options": options}
    )


# Additional mock utilities

class MockConfig:
    """Mock configuration management."""

    def __init__(self, config_path: str = None):
        self.config_path = config_path
        self.config_data = {
            "agent": {
                "name": "security-specialist",
                "model": "claude-3-opus",
                "temperature": 0.1
            },
            "tools": {
                "enabled": True,
                "timeout": 30
            }
        }

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value."""
        keys = key.split('.')
        value = self.config_data

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default

        return value

    def set(self, key: str, value: Any) -> None:
        """Set configuration value."""
        keys = key.split('.')
        config = self.config_data

        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]

        config[keys[-1]] = value


def load_mock_config(config_path: str = None) -> MockConfig:
    """Load mock configuration."""
    return MockConfig(config_path)