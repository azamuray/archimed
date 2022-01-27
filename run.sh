#!/bin/bash

venv="venv"

if [ ! -e $venv ]
then
      echo -e "\nInstalling Python dependencies..."
    python3 -m venv $venv
    source $venv/bin/activate
    pip install --upgrade pip > /dev/null
    pip install -r requirements.txt > /dev/null
    echo -e "[Success]"
fi

echo -e "\nRunning...\n"
source $venv/bin/activate
python main.py
