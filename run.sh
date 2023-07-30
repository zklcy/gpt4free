#!/bin/bash

# Check if the app.py process is running
if pgrep -f "interference/app.py" > /dev/null; then
    # If running, kill the existing app.py process
    echo "Stopping the existing app.py process..."
    kill $(pgrep -f "interference/app.py")
    sleep 2  # Wait for the process to terminate (adjust the time as needed)
fi

# Activate Python virtual environment
source ./venv/bin/activate

# Run app.py and redirect output to log.txt
echo "Starting app.py..."
nohup python3 interference/app.py >> log.txt 2>&1 &
