#!/bin/bash
# Synapse Global-First Setup
# Usage: ~/.synapse-system/setup [project-directory]

echo "🚀 Synapse System - Global-First Setup"
echo "======================================"
echo
echo "The setup system has been simplified!"
echo
echo "📦 For global services:"
echo "  synapse start"
echo
echo "🛠️  For project setup:"
echo "  synapse init ."
echo
echo "📚 For searching knowledge:"
echo "  synapse search \"query\""
echo
echo "🔄 For project updates:"
echo "  synapse update"
echo
echo "✨ Full usage:"
echo "  synapse --help"
echo

# If a directory is provided, initialize it
if [[ -n "$1" ]] && [[ -d "$1" ]]; then
    echo "🔧 Initializing project: $1"
    exec ~/.synapse-system/bin/synapse init "$1"
elif [[ -n "$1" ]]; then
    echo "❌ Directory not found: $1"
    exit 1
else
    echo "💡 To setup current directory: synapse init ."
fi