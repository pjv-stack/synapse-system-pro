# Changelog

## [2025-09-17] - System Refactoring and Enhancement

This release includes a major refactoring of the Synapse agent system, as well as several new features and improvements.

### Added

*   **New Agents:**
    *   `@architect`: A new agent responsible for high-level system design and architecture.
    *   `@devops-engineer`: A new agent responsible for CI/CD, deployment, and infrastructure.
    *   `@ux-designer`: A new agent responsible for user experience and user interface design.
    *   `@security-specialist`: A new agent responsible for application security.
    *   `@docs-writer`: A new agent responsible for writing and maintaining documentation.
    *   `@planner`: A new agent responsible for decomposing high-level goals into actionable plans.
    *   `@tool-runner`: A new agent responsible for executing tools for other agents.
*   **`sync-agents.sh` script:** A new script to sync agent definitions from the `.synapse/agents` directory to the `.claude/agents` directory.
*   **`templates` directory:** A new directory to store modular file templates.
*   **`README.md` for core scripts:** A new `README.md` file in the `.synapse/neo4j/` directory to explain the purpose of the core scripts.
*   **`tool-mapping.json`:** A new file that defines the mapping between abstract tool names and their corresponding scripts.

### Changed

*   **Consolidated Agent Definitions:** All agent definitions are now located in the `.synapse/agents` directory. The `.claude/agents` directory is now populated by the `sync-agents.sh` script.
*   **Standardized Tool Definitions:** All agent definitions now use the high-level, abstract Synapse tools (`SynapseSearch`, `SynapseStandard`, `SynapseTemplate`, `SynapseHealth`).
*   **Updated `@synapse-project-manager`:** The `@synapse-project-manager` agent has been updated to be aware of the new team structure and to delegate tasks to the other agents.
*   **Simplified `@date-checker`:** The `@date-checker` agent has been simplified to use the `date` command.
*   **Modularized `@file-creator` templates:** The file templates have been moved from the `@file-creator` agent definition to the new `templates` directory.
*   **Improved `@git-workflow` error handling:** The `@git-workflow` agent now has a more robust error handling section.
*   **Improved `@test-runner` instructions:** The `@test-runner` agent now has more detailed, language-specific instructions for running tests.
*   **Improved Language Specialist collaboration:** The language specialist agents now have explicit instructions on how to collaborate with other team members.

### Removed

*   **Redundant `project-manager.md` agent:** The redundant `project-manager.md` agent has been removed from the `.claude/agents` directory.