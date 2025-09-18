#!/bin/bash
# Synapse System - Legacy Wrapper (.sh)
# Delegates to the new unified Python CLI for backward compatibility

set -e

SYNAPSE_HOME="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SYNAPSE_CLI="$SYNAPSE_HOME/bin/synapse"

# Check if new CLI exists
if [[ ! -f "$SYNAPSE_CLI" ]]; then
    echo "Error: New synapse CLI not found at $SYNAPSE_CLI" >&2
    echo "Please reinstall or run setup." >&2
    exit 1
fi

# Legacy wrapper - delegate all commands to new Python CLI
echo "🔄 Using legacy synapse.sh wrapper (consider using 'synapse' directly)"
exec "$SYNAPSE_CLI" "$@"