#!/bin/bash

# load environment variables
source ./enviroments.sh
if [ -f ./enviroments-user.sh ]; then
    source ./enviroments-user.sh
fi

# set venv directory
if [ -z "$VENV" ]; then
    echo "Virtual enviroment directory not set. Using default virtual enviroment directory..."
    VENV=$DEFAULT_VENV
fi

# set python interpreter
if [ -z "$PYTHON_INTERPRETER" ]; then
    echo "Python interpreter not set. Using default python interpreter..."
    PYTHON_INTERPRETER=$DEFAULT_PYTHON_INTERPRETER
fi

# set torch command
if [ -z "$TORCH_COMMAND" ]; then
    echo "torch command not set. Using default torch command..."
    TORCH_COMMAND=$DEFAULT_TORCH_COMMAND
fi

# create venv directory
if [ ! -d "$VENV" ]; then
    echo "Creating virtual enviroment directory..."
    $PYTHON_INTERPRETER -m venv $VENV
fi

# activate venv
source $VENV/bin/activate

# check torch installation
if ! python -c "import torch" &> /dev/null; then
    echo "Installing torch..."
    $TORCH_COMMAND
fi

# check requirements is installed
pip install -r requirements.txt --quiet

# run the script
$PYTHON_INTERPRETER "server.py"