"""
Test configuration and fixtures for Synapse System

This module provides pytest fixtures for testing with isolated
Redis and Neo4j containers using testcontainers.
"""

import pytest
import redis
import subprocess
import sys
from pathlib import Path
from neo4j import GraphDatabase
from testcontainers.redis import RedisContainer
from testcontainers.neo4j import Neo4jContainer
from typing import Generator, Dict, Any, NamedTuple


@pytest.fixture(scope="session")
def redis_container() -> Generator[Dict[str, Any], None, None]:
    """
    Provides a Redis container for testing.

    Yields:
        Dict containing Redis connection details:
        - host: Container host
        - port: Container port
        - client: Redis client instance
    """
    with RedisContainer("redis:7-alpine") as container:
        # Get connection details
        host = container.get_container_host_ip()
        port = container.get_exposed_port(6379)

        # Create Redis client
        client = redis.Redis(
            host=host,
            port=port,
            decode_responses=True,
            socket_connect_timeout=30,
            socket_timeout=30
        )

        # Wait for Redis to be ready
        container.exec("redis-cli ping")

        yield {
            "host": host,
            "port": port,
            "client": client,
            "url": f"redis://{host}:{port}"
        }


@pytest.fixture(scope="session")
def neo4j_container() -> Generator[Dict[str, Any], None, None]:
    """
    Provides a Neo4j container for testing.

    Yields:
        Dict containing Neo4j connection details:
        - host: Container host
        - port: Container port (bolt protocol)
        - http_port: Container HTTP port
        - username: Neo4j username
        - password: Neo4j password
        - driver: Neo4j driver instance
        - bolt_url: Bolt connection URL
        - http_url: HTTP connection URL
    """
    with Neo4jContainer("neo4j:5.13") as container:
        # Get connection details
        host = container.get_container_host_ip()
        bolt_port = container.get_exposed_port(7687)
        http_port = container.get_exposed_port(7474)
        username = container.username
        password = container.password

        # Create Neo4j driver
        bolt_url = f"bolt://{host}:{bolt_port}"
        driver = GraphDatabase.driver(
            bolt_url,
            auth=(username, password)
        )

        # Verify connection
        with driver.session() as session:
            session.run("RETURN 1")

        yield {
            "host": host,
            "bolt_port": bolt_port,
            "http_port": http_port,
            "username": username,
            "password": password,
            "driver": driver,
            "bolt_url": bolt_url,
            "http_url": f"http://{host}:{http_port}"
        }

        # Cleanup
        driver.close()


@pytest.fixture
def redis_client(redis_container):
    """
    Provides a fresh Redis client for each test.

    The client is automatically flushed before each test.
    """
    client = redis_container["client"]
    client.flushall()  # Clean slate for each test
    return client


@pytest.fixture
def neo4j_session(neo4j_container):
    """
    Provides a fresh Neo4j session for each test.

    The database is automatically cleared before each test.
    """
    driver = neo4j_container["driver"]

    with driver.session() as session:
        # Clear the database
        session.run("MATCH (n) DETACH DELETE n")
        yield session


class CLIResult(NamedTuple):
    """Result from CLI command execution."""
    stdout: str
    stderr: str
    exit_code: int


@pytest.fixture
def cli_runner():
    """
    Provides a CLI runner for executing Synapse commands.

    Returns a function that executes synapse commands and returns
    CLIResult with stdout, stderr, and exit_code.
    """
    def run_command(*args, cwd=None, timeout=30):
        """
        Execute a synapse command.

        Args:
            *args: Command arguments (e.g., 'init', '.')
            cwd: Working directory for command execution
            timeout: Command timeout in seconds

        Returns:
            CLIResult: Named tuple with stdout, stderr, exit_code
        """
        # Path to the CLI script
        cli_script = Path(__file__).parent.parent / "lib" / "cli.py"

        # Build command
        cmd = [sys.executable, str(cli_script)] + list(args)

        try:
            result = subprocess.run(
                cmd,
                cwd=cwd,
                capture_output=True,
                text=True,
                timeout=timeout
            )

            return CLIResult(
                stdout=result.stdout,
                stderr=result.stderr,
                exit_code=result.returncode
            )

        except subprocess.TimeoutExpired:
            return CLIResult(
                stdout="",
                stderr=f"Command timed out after {timeout} seconds",
                exit_code=-1
            )
        except Exception as e:
            return CLIResult(
                stdout="",
                stderr=f"Command execution failed: {str(e)}",
                exit_code=-1
            )

    return run_command