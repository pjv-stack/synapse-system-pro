"""
Mock Claude Code SDK

Fallback implementation for development and testing when the actual SDK is not available.
Provides the same interface as the real SDK for seamless development.
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
    """Mock MCP Server for development."""

    def __init__(self, name: str, tools: List[MockTool]):
        self.name = name
        self.tools = {tool.name: tool for tool in tools}
        self.running = False

    async def run(self):
        """Mock server run method."""
        self.running = True
        print(f"🔧 Mock MCP Server '{self.name}' started with {len(self.tools)} tools")

    async def stop(self):
        """Mock server stop method."""
        self.running = False
        print(f"🔧 Mock MCP Server '{self.name}' stopped")

    def get_available_tools(self) -> List[str]:
        """Get list of available tools."""
        return list(self.tools.keys())

def create_sdk_mcp_server(name: str, tools: List[Callable]) -> MockMCPServer:
    """
    Create a mock MCP server with tools.

    Args:
        name: Server name
        tools: List of tool functions

    Returns:
        Mock MCP server instance
    """
    mock_tools = []
    for tool_func in tools:
        tool_name = tool_func.__name__
        tool_desc = tool_func.__doc__ or "No description"
        mock_tools.append(MockTool(name=tool_name, func=tool_func, description=tool_desc))

    return MockMCPServer(name, mock_tools)

def tool(func: Callable) -> Callable:
    """
    Mock tool decorator.

    Marks a function as a tool that can be called by Claude Code.
    In the real SDK, this would register the tool with the MCP server.
    """
    # Add tool metadata
    func._is_tool = True
    func._tool_name = func.__name__
    func._tool_description = func.__doc__ or "No description provided"

    # Add some mock validation
    def wrapper(*args, **kwargs):
        print(f"🔧 Mock tool '{func.__name__}' called")
        return func(*args, **kwargs)

    # Preserve original function attributes
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    wrapper._is_tool = True
    wrapper._tool_name = func._tool_name
    wrapper._tool_description = func._tool_description

    return wrapper

async def query(prompt: str, options: Optional[Dict[str, Any]] = None) -> AsyncGenerator[ClaudeCodeSdkMessage, None]:
    """
    Mock query function that simulates Claude Code SDK query.

    Args:
        prompt: Prompt to send
        options: Optional query options

    Yields:
        Mock messages from Claude
    """
    print(f"🔧 Mock query: {prompt[:50]}{'...' if len(prompt) > 50 else ''}")

    # Simulate some processing delay
    await asyncio.sleep(0.1)

    # Yield mock responses
    mock_responses = [
        {
            "type": "message",
            "content": "Hello! I'm Code Hound, ready to enforce quality standards.",
            "metadata": {"source": "mock_sdk"}
        },
        {
            "type": "tool_request",
            "tool": "comprehensive_code_review",
            "args": {"file_path": "./example.py", "review_type": "full"},
            "metadata": {"source": "mock_sdk"}
        }
    ]

    for response in mock_responses:
        yield response
        await asyncio.sleep(0.05)  # Small delay between responses

class MockClaudeClient:
    """Mock Claude client for testing."""

    def __init__(self, model: str = "claude-3-sonnet"):
        self.model = model
        self.request_count = 0

    async def send_message(self, content: str, system_prompt: Optional[str] = None) -> str:
        """Send a mock message and get response."""
        self.request_count += 1
        print(f"🔧 Mock message to {self.model}: {content[:30]}...")

        # Simulate processing delay
        await asyncio.sleep(0.1)

        # Generate mock response based on content
        if "review" in content.lower():
            return "Here's my code review analysis..."
        elif "test" in content.lower():
            return "TDD compliance check complete..."
        elif "solid" in content.lower():
            return "SOLID principles analysis..."
        else:
            return "Mock response from Code Hound"

    def get_usage_stats(self) -> Dict[str, Any]:
        """Get mock usage statistics."""
        return {
            "model": self.model,
            "requests_made": self.request_count,
            "total_tokens": self.request_count * 150,  # Mock token usage
            "cost_estimate": self.request_count * 0.01  # Mock cost
        }

# Mock configuration and environment
class MockEnvironment:
    """Mock environment for testing."""

    def __init__(self):
        self.variables = {
            "CLAUDE_API_KEY": "mock-api-key",
            "CLAUDE_MODEL": "claude-3-sonnet",
            "DEBUG": "true"
        }

    def get(self, key: str, default: Optional[str] = None) -> Optional[str]:
        """Get environment variable."""
        return self.variables.get(key, default)

    def set(self, key: str, value: str):
        """Set environment variable."""
        self.variables[key] = value

# Global mock instances
mock_env = MockEnvironment()
mock_client = MockClaudeClient()

# Mock utility functions
def is_claude_code_available() -> bool:
    """Check if real Claude Code SDK is available."""
    try:
        import claude_code_sdk
        return True
    except ImportError:
        return False

def get_mock_file_analysis(file_path: str) -> Dict[str, Any]:
    """Get mock file analysis for testing."""
    return {
        "file_path": file_path,
        "language": "python",
        "lines_of_code": 150,
        "complexity": {
            "cyclomatic_complexity": 8,
            "nesting_depth": 3
        },
        "violations": [
            {
                "type": "missing_tests",
                "severity": "critical",
                "line": 1,
                "message": "No test file found for this module"
            },
            {
                "type": "magic_number",
                "severity": "low",
                "line": 42,
                "message": "Magic number '42' should be named constant"
            }
        ],
        "scores": {
            "overall": 75,
            "tdd": 30,
            "solid": 80,
            "dry": 85,
            "kiss": 70
        }
    }

async def run_mock_analysis_demo():
    """Run a demonstration of mock analysis capabilities."""
    print("🐕 Code Hound Mock Analysis Demo")
    print("=" * 40)

    # Mock file analysis
    analysis = get_mock_file_analysis("example.py")
    print(f"Analyzing: {analysis['file_path']}")
    print(f"Language: {analysis['language']}")
    print(f"Lines of Code: {analysis['lines_of_code']}")
    print(f"Overall Score: {analysis['scores']['overall']}/100")

    if analysis['violations']:
        print(f"\nFound {len(analysis['violations'])} violations:")
        for violation in analysis['violations']:
            print(f"  - Line {violation['line']}: {violation['message']}")

    print("\nCode Hound verdict: Fix critical issues before proceeding!")

# Error simulation for testing
class MockSDKError(Exception):
    """Mock SDK error for testing error handling."""
    pass

def simulate_error(error_type: str = "network"):
    """Simulate various types of errors for testing."""
    if error_type == "network":
        raise MockSDKError("Mock network error - API unreachable")
    elif error_type == "auth":
        raise MockSDKError("Mock authentication error - Invalid API key")
    elif error_type == "rate_limit":
        raise MockSDKError("Mock rate limit error - Too many requests")
    else:
        raise MockSDKError(f"Mock {error_type} error")

# Mock performance monitoring
class MockPerformanceMonitor:
    """Mock performance monitoring for development."""

    def __init__(self):
        self.start_time = None
        self.metrics = {}

    def start_operation(self, operation_name: str):
        """Start monitoring an operation."""
        import time
        self.start_time = time.time()
        print(f"🔧 Started monitoring: {operation_name}")

    def end_operation(self, operation_name: str):
        """End monitoring an operation."""
        if self.start_time:
            import time
            duration = time.time() - self.start_time
            self.metrics[operation_name] = duration
            print(f"🔧 Operation '{operation_name}' took {duration:.2f}s")
            self.start_time = None

    def get_metrics(self) -> Dict[str, float]:
        """Get performance metrics."""
        return self.metrics.copy()

# Global mock monitor
mock_monitor = MockPerformanceMonitor()

if __name__ == "__main__":
    # Run demo if called directly
    asyncio.run(run_mock_analysis_demo())