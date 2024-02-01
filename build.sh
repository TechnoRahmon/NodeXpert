#!/bin/bash

# Get the directory where the script is located
DIR="$(pwd)"

# Change directory to the project directory
cd "$DIR"

# Log file
LOG_FILE="build.log"

# Function to log messages to the console and to the log file
log_message() {
    echo "$1"
    echo "$(date '+%Y-%m-%d %H:%M:%S') $1" >> "$LOG_FILE"
}

# Create virtual environment
log_message "Creating virtual environment..."
python -m venv .converter >> "$LOG_FILE" 2>&1

# Activate the virtual environment
log_message "Activating virtual environment..."
source .converter/Scripts/activate >> "$LOG_FILE" 2>&1

# Upgrade pip (optional)
log_message "Upgrading pip..."
py -m pip install --upgrade pip >> "$LOG_FILE" 2>&1

# Install requirements
log_message "Installing requirements..."
py -m pip install -r requirements.txt >> "$LOG_FILE" 2>&1

# Build the executable
log_message "Building the executable..."
pyinstaller --name NodeXpert --onefile --windowed --icon=icon.ico elevated_operations.py >> "$LOG_FILE" 2>&1

# Check if NodeXpert.exe exists in \dist directory
if [ -f "dist/NodeXpert.exe" ]; then
    echo "Build completed successfully. You can run the file in 'dist/NodeXpert.exe' to start the program."
else
    echo "Cannot build. Something went wrong."
fi

# Deactivate the virtual environment
log_message "Deactivating virtual environment..."
deactivate >> "$LOG_FILE" 2>&1

# Prompt user to close terminal
echo "Press any key to close this terminal..."
read -n 1 -s
