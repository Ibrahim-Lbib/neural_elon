# simple launcher for UNIX

#!/bin/bash

# Neural Elon – Unix/macOS/Linux launcher
# Save this exactly as: neural_elon/scripts/run.sh
# Then: chmod +x scripts/run.sh   (only once)

# Go to the project root (the folder that contains src/, data/, etc.)
cd "$(dirname "$0")/.." || exit 1

echo
echo "  Neural Elon is starting..."
echo

# Optional: activate virtual environment if it exists
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
    # Linux/macOS
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate    # Some Windows Git-Bash setups
fi

# Run the app
python -m src.main

# Friendly exit message
if [ $? -eq 0 ]; then
    echo
    echo "  Goodbye, rocketeer!"
else
    echo
    echo "  Something went wrong – check the error above."
fi

echo
read -p "  Press Enter to close..."  # keeps terminal open