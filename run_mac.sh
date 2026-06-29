#!/bin/bash
# ============================================================================
# Mac Runner Script
# ============================================================================
# This script runs the Python automation tool on Mac
# Requires: Chrome must be running with debugging (run launch_chrome_mac.sh first)
# ============================================================================

echo ""
echo "============================================================"
echo "One Press - Mac Version"
echo "============================================================"
echo ""

# Navigate to script directory
cd "$(dirname "$0")"

echo "Starting Python script..."
echo ""
echo "Note: You may be prompted for your password (sudo is required for keyboard library)"
echo ""

# Run with sudo (required for keyboard library on Mac)
sudo python3 onepress.py

read -p "Press Enter to exit..."

