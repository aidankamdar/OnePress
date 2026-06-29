# One Press - Mac Instructions

## Quick Setup (One-Time)

### Step 1: Make Scripts Executable

Open Terminal and run:

```bash
cd /path/to/onepress
chmod +x setup_mac.sh
./setup_mac.sh
```

This will:
- Make all scripts executable
- Install Python dependencies

### Step 2: Grant Accessibility Permissions

1. Go to **System Preferences** > **Security & Privacy** > **Privacy** tab
2. Click **Accessibility** in the left sidebar
3. Click the lock icon and enter your password
4. Add **Terminal** to the list (click + button)
5. Make sure the checkbox next to Terminal is checked

## Usage

### Every Time You Want to Use the Tool:

#### Method 1: Double-Click (Easiest)

1. **Double-click `launch_chrome_mac.command`** to start Chrome with debugging
2. Open Terminal and run:
   ```bash
   cd /path/to/onepress
   sudo python3 onepress.py
   ```
3. Enter your Mac password when prompted
4. Browse to a practice problem and press **'P'**

#### Method 2: Terminal Only

1. Open Terminal
2. Run all commands:
   ```bash
   cd /path/to/onepress
   ./launch_chrome_mac.sh &
   sleep 3
   sudo python3 onepress.py
   ```

#### Method 3: One-Line Command (Advanced)

```bash
cd /path/to/onepress && pkill -9 "Google Chrome" && sleep 1 && "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --remote-debugging-port=9222 --user-data-dir="/tmp/chrome-debug" > /dev/null 2>&1 & sleep 2 && sudo python3 onepress.py
```

## How It Works

1. Chrome launches with debugging enabled (port 9222)
2. Python script connects to Chrome
3. Press **'P'** on the practice problem you're working on
4. The problem is extracted and sent to OpenAI
5. The reference solution is copied to your clipboard
6. Press **Cmd+V** to paste it and compare against your own attempt

## Troubleshooting

### "Chrome not found"
- Make sure Chrome is installed in `/Applications/`
- If installed elsewhere, update the path in `launch_chrome_mac.sh`

### "Permission denied"
- Run: `chmod +x launch_chrome_mac.sh run_mac.sh`
- Make sure you granted Accessibility permissions

### "Keyboard library error"
- Make sure you're using `sudo` when running the Python script
- Check Accessibility permissions in System Preferences

### "Cannot connect to Chrome"
- Make sure Chrome was launched with debugging (using the .sh script)
- Close all Chrome windows and try again
- Check if port 9222 is blocked by firewall

### "pip3 not found"
- Install Python 3: https://www.python.org/downloads/
- Or use Homebrew: `brew install python3`

## Requirements

- macOS 10.13 or later
- Python 3.7 or later
- Google Chrome
- Terminal with Accessibility permissions

## Notes

- The `keyboard` library requires `sudo` on Mac (administrator privileges)
- You'll need to enter your password each time you run the script
- Chrome must be launched with the provided script (not normally)
- Keep the Chrome window open while using the tool

## Alternative: Create an Application

To avoid Terminal, you can create an Automator application:

1. Open **Automator**
2. Create new **Application**
3. Add "Run Shell Script" action
4. Paste the one-line command above
5. Save as "One Press.app"
6. Double-click the app to run!
