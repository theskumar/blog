#!/bin/bash
set -e

# Install uv if it's not already installed
if ! command -v uv &> /dev/null; then
    echo "Installing uv package manager..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # Reload the shell to include the updated PATH
    source ~/.bashrc || source ~/.zshrc
fi

# Create a virtual environment and install dependencies
echo "Setting up virtual environment and installing dependencies..."
uv sync

echo "Setup complete! Run 'source .venv/bin/activate' to activate the environment."
echo "Then use 'make devserver' to start the development server."
