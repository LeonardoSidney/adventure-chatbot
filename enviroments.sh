#!/bin/bash
# Description: This file contains the default values for the enviroment variables used in the scripts.

# Set venv directory
export DEFAULT_VENV="venv"

# Set python interpreter
export DEFAULT_PYTHON_INTERPRETER="python3.12"

# Set torch command
export DEFAULT_TORCH_COMMAND="pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.2"