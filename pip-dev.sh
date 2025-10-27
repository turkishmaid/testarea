#!/bin/bash

which python3

# exit when "/venv" is not in the output of `which python3`
if [[ $(which python3) != *"/venv"* ]]; then
    echo "Please activate the virtual environment first."
    exit 1
fi

pip install -e ~/clonezoo/github/turkishmaid/anita
