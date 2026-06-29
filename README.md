# One Press - Coding Practice Solution Helper

A hotkey-activated study aid for working through coding-practice problems. When you're stuck on a problem from an open practice site, one press extracts the prompt, asks AI for a reference solution, and copies it to your clipboard so you can compare it against your own attempt.

> **Scope:** Built for self-study on open practice platforms like LeetCode, HackerRank, Codewars, and Project Euler. It is **not** for graded coursework, quizzes, or exams — see the [disclaimer](#disclaimer).

## Features

- ⌨️ **One Keypress**: Press the hotkey on a practice problem to get a reference solution
- 💻 **Practice-Focused**: Tuned for open coding sites (LeetCode, HackerRank, Codewars, Project Euler)
- 🤖 **AI-Powered**: Uses OpenAI GPT-4o for accurate solutions
- 📋 **Instant Clipboard**: Solutions automatically copied and ready to paste
- 🎯 **Auto-Detection**: Finds the problem statement across common practice-site layouts
- 🔄 **Background Service**: Runs continuously, ready whenever you need it

## How It Works

1. Launch Chrome with debugging enabled (one-time setup)
2. Start the script (runs in background)
3. Browse to a practice problem you're working on
4. Press **'P'** to extract the problem and get a reference solution
5. Press **Ctrl+V** to paste it and compare against your own work

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Note**: The `keyboard` library requires administrator privileges on Windows.

### 2. Ensure Chrome is Installed

The script connects to your existing Chrome browser (no special setup needed).

## Configuration (Optional)

The script works out-of-the-box, but you can customize settings in `onepress.py`:

### Change the Hotkey

```python
HOTKEY = "p"  # Change to any key: "f9", "ctrl+shift+s", etc.
```

### Change AI Model

```python
OPENAI_MODEL = "gpt-4o"        # Most capable (default)
OPENAI_MODEL = "gpt-4o-mini"   # Faster, cheaper
```

## Usage

### Step 1: Launch Chrome with Debugging

**Double-click `launch_chrome.bat`** (Windows)

This opens Chrome with remote debugging enabled. Browse normally in this window.

**For Mac/Linux users:** Create a similar script or run:
```bash
# Mac
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="$HOME/Library/Application Support/Google/Chrome"

# Linux
google-chrome --remote-debugging-port=9222 --user-data-dir="$HOME/.config/google-chrome"
```

### Step 2: Start One Press

Open a terminal/PowerShell and run:

```bash
python onepress.py
```

**Important**: Run as administrator on Windows (right-click PowerShell → "Run as administrator")

You should see:
```
✨ Ready! Press 'P' on any webpage to solve the problem
```

### Step 3: Use It!

1. Navigate to a practice problem you're working on
2. Press **'P'** on your keyboard
3. Wait a few seconds while the reference solution is generated
4. The solution is automatically copied to your clipboard
5. Press **Ctrl+V** to paste it and compare against your own attempt

## Troubleshooting

### ❌ "Error connecting to Chrome"

**Problem**: Script can't connect to Chrome

**Solutions**:
- Make sure you launched Chrome using the launcher script (not the normal Chrome icon)
- Check that Chrome is still running
- Verify no firewall is blocking port 9222
- Try closing all Chrome windows and re-running the launcher

### ❌ "Failed to extract problem"

**Problem**: Script can't find the problem text on the page

**Solutions**:
- Make sure the page has loaded fully before pressing the hotkey
- Check that the page contains visible text content
- Try refreshing the page and pressing the hotkey again

### ❌ "requires administrator privileges" (Windows)

**Problem**: Keyboard library needs admin rights

**Solution**:
- Close PowerShell/CMD
- Right-click PowerShell → "Run as administrator"
- Navigate to the One Press folder
- Run: `python onepress.py`

### ❌ "API key file not found"

**Problem**: Can't find `apikey.txt`

**Solution**:
- Ensure `apikey.txt` is in the same folder as the script
- Check that the file contains your OpenAI API key
- No extra spaces or newlines in the file

### ⚠️ Hotkey Not Working

**Problem**: Pressing the hotkey doesn't do anything

**Solutions**:
- Make sure the Python script is running (check the terminal)
- Verify you ran the script as administrator on Windows
- Try changing the hotkey to something else (like "f9") in the config
- Check if another program is intercepting the key

## Tips & Best Practices

1. **Keep Chrome Window Open**: Don't close the Chrome window launched by the script
2. **Run Script Once**: The script runs continuously - no need to restart for each problem
3. **Wait for Completion**: Give it a few seconds to process before trying again
4. **Check Terminal**: Watch the terminal for status messages and errors

## Security & Privacy

- ✅ Your API key is stored locally and never shared
- ✅ The script only reads the current page when you press the hotkey
- ✅ No data is stored or logged
- ⚠️ Keep `apikey.txt` secure and never commit it to version control (it's in `.gitignore`)

## Disclaimer

This tool is intended for **self-study on open coding-practice platforms** — reviewing reference solutions to learn from after you've attempted a problem yourself. It is **not** intended for graded coursework, quizzes, exams, or any setting where getting outside help would violate an academic integrity policy or a site's terms of use. You're responsible for using it honestly and within the rules that apply to you.
