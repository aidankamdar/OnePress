#!/bin/bash
# ============================================================================
# Chrome Launcher with Remote Debugging (Mac Version)
# ============================================================================
# This script launches Chrome with remote debugging enabled on port 9222.
# This allows the Python script to connect to your existing Chrome browser.
#
# Usage: Run this file in Terminal, then run the Python script.
# ============================================================================

echo ""
echo "============================================================"
echo "Chrome Launcher with Remote Debugging (Mac)"
echo "============================================================"
echo ""

# Find Chrome installation
CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

if [ ! -f "$CHROME_PATH" ]; then
    echo "ERROR: Chrome not found at: $CHROME_PATH"
    echo ""
    echo "Please install Google Chrome or update this script with your Chrome path."
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

echo "Found Chrome at: $CHROME_PATH"
echo ""

# Close any existing Chrome processes
echo "Checking for running Chrome processes..."
pkill -9 "Google Chrome" 2>/dev/null
sleep 1
echo "Chrome processes closed (if any were running)"
echo ""

# Launch Chrome with debugging
echo "Launching Chrome with debugging on port 9222..."
echo ""
"$CHROME_PATH" --remote-debugging-port=9222 --user-data-dir="/tmp/chrome-debug-profile" &

# Wait for Chrome to start
sleep 2

echo ""
echo "============================================================"
echo "SUCCESS! Chrome is running with debugging enabled"
echo "============================================================"
echo ""
echo "NEXT STEPS:"
echo "1. Browse to any webpage with a problem"
echo "2. Open a new Terminal window"
echo "3. Navigate to the One Press folder"
echo "4. Run: sudo python3 onepress.py"
echo "5. Press 'P' on any webpage to solve it"
echo ""
echo "Keep this window open!"
echo ""
read -p "Press Enter to continue..."

