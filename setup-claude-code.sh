#!/bin/bash
# Claude Code Setup - Now Simplified!
# Usage: setup-claude-code [project-directory]

echo "🎯 Claude Code + Synapse Setup"
echo "==============================="
echo
echo "The setup has been greatly simplified!"
echo
echo "Just run: ~/.synapse-system/synapse init ."
echo

# Delegate to the new simple system
if [[ -n "$1" ]]; then
    exec ~/.synapse-system/synapse.sh init "$1"
else
    exec ~/.synapse-system/synapse init .
fi