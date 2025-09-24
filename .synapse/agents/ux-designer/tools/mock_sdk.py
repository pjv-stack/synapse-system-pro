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
        print(f"🎨 Mock MCP Server '{name}' initialized with {len(tools)} UX/UI tools")

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
    func._tool_description = func.__doc__ or f"UX tool: {func.__name__}"

    print(f"🔧 Registered UX tool: {func.__name__}")

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

    print(f"🤔 Mock UX query received: {prompt[:100]}{'...' if len(prompt) > 100 else ''}")

    # Simulate a UX-focused response
    response = f"Mock UX analysis for: {prompt[:50]}{'...' if len(prompt) > 50 else ''}"

    yield ClaudeCodeSdkMessage(
        role="ux_designer",
        content=response,
        metadata={"mock": True, "domain": "ux_design", "options": options}
    )


# Additional mock utilities for UX work

class MockDesignConfig:
    """Mock configuration management for design workflows."""

    def __init__(self, config_path: str = None):
        self.config_path = config_path
        self.config_data = {
            "agent": {
                "name": "ux-designer",
                "model": "claude-3-sonnet",
                "temperature": 0.2,
                "focus": "user_experience"
            },
            "design_preferences": {
                "style": "modern",
                "accessibility": "wcag_aa",
                "mobile_first": True
            },
            "tools": {
                "enabled": True,
                "timeout": 45,
                "design_validation": True
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


class MockDesignAssets:
    """Mock design asset management."""

    def __init__(self):
        self.assets = {
            "color_palettes": [
                {"name": "primary", "colors": ["#007bff", "#0056b3", "#004085"]},
                {"name": "secondary", "colors": ["#6c757d", "#5a6268", "#495057"]},
                {"name": "success", "colors": ["#28a745", "#1e7e34", "#155724"]}
            ],
            "typography": [
                {"name": "headings", "font": "Inter", "weights": [400, 600, 700]},
                {"name": "body", "font": "Inter", "weights": [400, 500]},
                {"name": "monospace", "font": "Monaco", "weights": [400]}
            ],
            "spacing_scale": [4, 8, 16, 24, 32, 48, 64, 96],
            "breakpoints": {
                "mobile": "320px",
                "tablet": "768px",
                "desktop": "1024px",
                "wide": "1440px"
            }
        }

    def get_palette(self, name: str) -> Dict[str, Any]:
        """Get color palette by name."""
        for palette in self.assets["color_palettes"]:
            if palette["name"] == name:
                return palette
        return {"name": "default", "colors": ["#000000", "#ffffff"]}

    def get_typography(self) -> List[Dict[str, Any]]:
        """Get typography specifications."""
        return self.assets["typography"]

    def get_spacing_scale(self) -> List[int]:
        """Get spacing scale."""
        return self.assets["spacing_scale"]

    def get_breakpoints(self) -> Dict[str, str]:
        """Get responsive breakpoints."""
        return self.assets["breakpoints"]


def load_mock_config(config_path: str = None) -> MockDesignConfig:
    """Load mock configuration for UX designer."""
    return MockDesignConfig(config_path)


def load_design_assets() -> MockDesignAssets:
    """Load mock design assets."""
    return MockDesignAssets()


# Mock user research data
class MockUserData:
    """Mock user research data for testing and development."""

    def __init__(self):
        self.personas = [
            {
                "name": "Sarah Product Manager",
                "age": "29",
                "role": "Product Manager at tech startup",
                "goals": ["Launch features quickly", "Understand user needs", "Coordinate team"],
                "pain_points": ["Too many meetings", "Unclear requirements", "Tool switching"],
                "tech_comfort": "High",
                "devices": ["MacBook Pro", "iPhone"],
                "quote": "I need tools that help me make decisions based on data, not gut feelings."
            },
            {
                "name": "Mike Developer",
                "age": "24",
                "role": "Frontend Developer",
                "goals": ["Write clean code", "Learn new technologies", "Ship features"],
                "pain_points": ["Unclear designs", "Changing requirements", "Browser compatibility"],
                "tech_comfort": "Very High",
                "devices": ["Custom PC", "Android phone"],
                "quote": "Give me clear specs and I'll build it. But please, no more last-minute changes."
            },
            {
                "name": "Lisa Marketing Director",
                "age": "35",
                "role": "Marketing Director",
                "goals": ["Increase brand awareness", "Generate leads", "Measure ROI"],
                "pain_points": ["Scattered data", "Complex tools", "Proving marketing value"],
                "tech_comfort": "Medium",
                "devices": ["MacBook Air", "iPhone"],
                "quote": "I love data, but I need it presented in a way that tells a story."
            }
        ]

        self.user_feedback = [
            {
                "user_id": "user_001",
                "feedback": "The interface is clean but I'm not sure where to find advanced features",
                "sentiment": "neutral",
                "category": "navigation"
            },
            {
                "user_id": "user_002",
                "feedback": "Love how fast it loads, but the color contrast could be better",
                "sentiment": "positive",
                "category": "accessibility"
            },
            {
                "user_id": "user_003",
                "feedback": "Getting started was confusing, needed help to complete my first task",
                "sentiment": "negative",
                "category": "onboarding"
            }
        ]

    def get_personas(self) -> List[Dict[str, Any]]:
        """Get mock user personas."""
        return self.personas

    def get_user_feedback(self) -> List[Dict[str, Any]]:
        """Get mock user feedback data."""
        return self.user_feedback

    def get_usability_metrics(self) -> Dict[str, Any]:
        """Get mock usability metrics."""
        return {
            "task_success_rate": 78,
            "time_on_task": 145,  # seconds
            "error_rate": 12,
            "satisfaction_score": 7.2,
            "net_promoter_score": 42
        }


def load_user_data() -> MockUserData:
    """Load mock user research data."""
    return MockUserData()