#!/bin/bash
# ============================================================================
# Mac Setup Script
# ============================================================================
# This script makes the launcher scripts executable and installs dependencies
# ============================================================================

echo ""
echo "============================================================"
echo "One Press - Setup"
echo "============================================================"
echo ""

# Navigate to script directory
cd "$(dirname "$0")"

echo "Making scripts executable..."
chmod +x launch_chrome_mac.sh
chmod +x launch_chrome_mac.command
chmod +x run_mac.sh
echo "✓ Scripts are now executable"
echo ""

echo "Installing Python dependencies..."
echo ""

# Check if pip3 is available
if command -v pip3 &> /dev/null; then
    pip3 install -r requirements.txt
else
    echo "WARNING: pip3 not found. Please install Python 3 first."
    echo "Visit: https://www.python.org/downloads/"
fi

echo ""
echo "============================================================"
echo "Setup Complete!"
echo "============================================================"
echo ""
echo "IMPORTANT: Grant Accessibility Permissions"
echo "-------------------------------------------"
echo "The keyboard library needs accessibility permissions on Mac."
echo ""
echo "When you run the script, macOS will prompt you to allow"
echo "Terminal in System Preferences > Security & Privacy > Accessibility"
echo ""
echo "NEXT STEPS:"
echo "1. Double-click 'launch_chrome_mac.command' to start Chrome"
echo "2. In Terminal, run: sudo python3 onepress.py"
echo "3. Press 'P' on any webpage to solve it"
echo ""
read -p "Press Enter to finish..."

