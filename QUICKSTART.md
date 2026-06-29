# Quick Start Guide

## 3-Step Setup

### 1️⃣ Install Dependencies

Open PowerShell **as Administrator** and run:

```powershell
cd path\to\onepress
pip install -r requirements.txt
```

### 2️⃣ Launch Chrome with Debugging

Double-click **`launch_chrome.bat`**

This opens Chrome in a special mode. Keep this window open and browse to the practice problem you're working on.

### 3️⃣ Start One Press

In the same PowerShell (as Administrator), run:

```powershell
python onepress.py
```

You should see:
```
✨ Ready! Open a practice problem and press 'P' for a reference solution
```

## How to Use

1. **Navigate** to a practice problem you're working on
2. **Press 'P'** on your keyboard
3. **Wait** 3-5 seconds for the reference solution to be generated
4. **Press Ctrl+V** to paste it and compare against your own attempt

That's it! The solution is automatically in your clipboard.

## Example Workflow

```
You: Browse to a practice problem you're working on
You: Press 'P'
Script: ⚡ One Press - Processing problem...
Script: ✓ Extracted 1234 characters
Script: 🤖 Sending to OpenAI GPT-4o...
Script: ✓ Solution received!
Script: 📋 Copied to clipboard!
Script: ✅ Done! Solution copied to clipboard - press Ctrl+V to paste
You: Press Ctrl+V anywhere to paste the solution
```

## Important Notes

⚠️ **Run as Administrator**: The keyboard library requires admin privileges on Windows

⚠️ **Keep Chrome Open**: Don't close the Chrome window launched by `launch_chrome.bat`

⚠️ **One-Time Setup**: Once running, the script works on any webpage - no need to restart

## Common Issues

### "Error connecting to Chrome"
→ Make sure you ran `launch_chrome.bat` first

### "requires administrator privileges"
→ Right-click PowerShell → "Run as administrator"

### Hotkey not working
→ Make sure the script is running and you ran PowerShell as admin

## Need Help?

Check the full README.md for detailed troubleshooting and configuration options.
