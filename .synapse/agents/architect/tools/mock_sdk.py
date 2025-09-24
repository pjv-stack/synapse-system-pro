"""Mock SDK for Architect Development"""

import asyncio
from typing import Any, AsyncGenerator, Dict, Callable
from dataclasses import dataclass

ClaudeCodeSdkMessage = Dict[str, Any]

@dataclass
class MockTool:
    name: str
    func: Callable
    description: str = ""

class MockMCPServer:
    def __init__(self, name: str, tools: list):
        self.name = name
        self.tools = {tool.name: tool for tool in tools}

    async def run(self):
        print(f"🏛️ Mock Architect Server '{self.name}' started with {len(self.tools)} tools")

def create_sdk_mcp_server(name: str, tools: list) -> MockMCPServer:
    mock_tools = []
    for tool_func in tools:
        mock_tools.append(MockTool(name=tool_func.__name__, func=tool_func))
    return MockMCPServer(name, mock_tools)

def tool(func: Callable) -> Callable:
    func._is_tool = True
    return func

async def query(prompt: str) -> AsyncGenerator[ClaudeCodeSdkMessage, None]:
    await asyncio.sleep(0.1)
    yield {"type": "message", "content": "Architect agent ready for system design"}