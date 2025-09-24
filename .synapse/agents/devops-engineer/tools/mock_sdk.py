"""
Mock Claude Code SDK for DevOps Engineer Agent development/testing purposes.
This provides fallback implementations when the real SDK is not available.
"""

from typing import Any, AsyncGenerator, Dict, List, Callable
import json

# Mock types
ClaudeCodeSdkMessage = Dict[str, Any]

class MockMCPServer:
    """Mock MCP server for testing."""
    def __init__(self, name: str, version: str, tools: List[Callable]):
        self.name = name
        self.version = version
        self.tools = {tool.__name__: tool for tool in tools}

def create_sdk_mcp_server(name: str, version: str, tools: List[Callable]) -> MockMCPServer:
    """Create a mock MCP server."""
    return MockMCPServer(name, version, tools)

def tool(func: Callable) -> Callable:
    """Mock tool decorator."""
    func._is_tool = True
    return func

async def query(prompt: AsyncGenerator[ClaudeCodeSdkMessage, None], options: Dict = None) -> AsyncGenerator[Dict[str, Any], None]:
    """
    Mock query function that simulates DevOps agent responses.
    In a real implementation, this would connect to Claude.
    """
    # Collect the prompt
    prompt_messages = []
    async for msg in prompt:
        prompt_messages.append(msg)

    # Simulate processing
    yield {
        "type": "thought",
        "thought": "Analyzing DevOps request and determining appropriate tools and strategies..."
    }

    # Extract user message
    if prompt_messages:
        user_content = prompt_messages[0].get("message", {}).get("content", "")

        # DevOps-specific mock responses based on content
        if "docker" in user_content.lower() or "container" in user_content.lower():
            yield {
                "type": "tool_use",
                "name": "manage_containers"
            }
            response_text = "🐳 Container Management Active\n\nAnalyzing container requirements and preparing Docker operations.\n\nReady to build, deploy, or manage containerized applications."

        elif "deploy" in user_content.lower() or "deployment" in user_content.lower():
            yield {
                "type": "tool_use",
                "name": "deploy_to_environment"
            }
            response_text = "🚀 Deployment Pipeline Ready\n\nEvaluating deployment strategy and target environment.\n\nPreparing for automated deployment with health checks and rollback capabilities."

        elif "monitor" in user_content.lower() or "health" in user_content.lower():
            yield {
                "type": "tool_use",
                "name": "setup_monitoring"
            }
            response_text = "📊 Monitoring System Active\n\nConfiguring observability stack and health check endpoints.\n\nSetting up comprehensive monitoring with alerts and dashboards."

        elif "infrastructure" in user_content.lower() or "terraform" in user_content.lower():
            yield {
                "type": "tool_use",
                "name": "provision_resources"
            }
            response_text = "🏗️ Infrastructure as Code Ready\n\nAnalyzing infrastructure requirements and preparing resource provisioning.\n\nReady to deploy scalable, secure infrastructure configurations."

        elif "ci/cd" in user_content.lower() or "pipeline" in user_content.lower():
            yield {
                "type": "tool_use",
                "name": "configure_ci_cd"
            }
            response_text = "⚙️ CI/CD Pipeline Configuration\n\nDesigning automated build, test, and deployment workflows.\n\nOptimizing for speed, reliability, and deployment safety."

        elif "dockerfile" in user_content.lower() or "image" in user_content.lower():
            yield {
                "type": "tool_use",
                "name": "create_dockerfile"
            }
            response_text = "📋 Dockerfile Generation Active\n\nCreating optimized, secure container definitions.\n\nImplementing multi-stage builds and security best practices."

        elif "logs" in user_content.lower() or "analyze" in user_content.lower():
            yield {
                "type": "tool_use",
                "name": "analyze_logs"
            }
            response_text = "🔍 Log Analysis in Progress\n\nProcessing log data and identifying patterns, errors, and performance insights.\n\nGenerating actionable recommendations based on log analysis."

        elif "alert" in user_content.lower() or "notification" in user_content.lower():
            yield {
                "type": "tool_use",
                "name": "create_alerts"
            }
            response_text = "🚨 Alert System Configuration\n\nSetting up intelligent alerting with proper escalation policies.\n\nConfiguring notifications to reduce noise and ensure rapid response."

        elif "scan" in user_content.lower() or "security" in user_content.lower():
            yield {
                "type": "tool_use",
                "name": "scan_infrastructure"
            }
            response_text = "🛡️ Security Scanning Active\n\nPerforming comprehensive security analysis of infrastructure and containers.\n\nIdentifying vulnerabilities and providing remediation guidance."

        elif "report" in user_content.lower() or "metrics" in user_content.lower():
            yield {
                "type": "tool_use",
                "name": "generate_reports"
            }
            response_text = "📈 Performance Reporting\n\nGenerating comprehensive reports on system performance, availability, and costs.\n\nProviding insights for optimization and capacity planning."

        else:
            response_text = "⚙️ DevOps Engineer Ready\n\nI can help you with:\n\n🐳 Container management and Docker operations\n🚀 Deployment strategies and automation\n📊 Monitoring and observability setup\n🏗️ Infrastructure as Code (Terraform, CloudFormation)\n⚙️ CI/CD pipeline configuration\n🔍 Log analysis and troubleshooting\n🛡️ Security scanning and compliance\n📈 Performance reporting and optimization\n\nWhat would you like to work on?"

    # Final response
    yield {
        "type": "result",
        "subtype": "success",
        "result": {
            "content": [{
                "type": "text",
                "text": response_text
            }]
        }
    }