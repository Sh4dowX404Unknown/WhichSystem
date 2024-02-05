#!/bin/bash

# This script is designed to move a Python script (whichsystem.py) to the /usr/local/bin directory
# and give it executable permissions.

# Move the Python script to /usr/local/bin
sudo mv whichsystem.py /usr/local/bin

# Give the script executable permissions
sudo chmod +x /usr/local/bin/whichsystem.py

# Remove folder
cd ..
rm -rf WhichSystem
