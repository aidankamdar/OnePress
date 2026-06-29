@echo off
title Chrome Debugger Launcher

echo.
echo ============================================================
echo Chrome Launcher with Remote Debugging
echo ============================================================
echo.

REM Find Chrome installation
set CHROME_PATH=

if exist "C:\Program Files\Google\Chrome\Application\chrome.exe" (
    set CHROME_PATH=C:\Program Files\Google\Chrome\Application\chrome.exe
)

if exist "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" (
    set CHROME_PATH=C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
)

if exist "%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe" (
    set CHROME_PATH=%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe
)

if "%CHROME_PATH%"=="" (
    echo ERROR: Chrome not found!
    echo.
    pause
    exit
)

echo Found Chrome at: %CHROME_PATH%
echo.

REM Close any existing Chrome processes
echo Checking for running Chrome processes...
taskkill /F /IM chrome.exe >nul 2>&1
timeout /t 1 /nobreak >nul
echo Chrome processes closed (if any were running)
echo.

REM Launch Chrome with debugging
echo Launching Chrome with debugging on port 9222...
echo.
start "" "%CHROME_PATH%" --remote-debugging-port=9222 --user-data-dir="%TEMP%\chrome-debug-profile"

REM Wait for Chrome to start
timeout /t 2 /nobreak >nul

echo.
echo ============================================================
echo SUCCESS! Chrome is running with debugging enabled
echo ============================================================
echo.
echo NEXT STEPS:
echo 1. Browse to any webpage with a problem
echo 2. Open PowerShell AS ADMINISTRATOR
echo 3. Navigate to the One Press folder
echo 4. Run: python onepress.py
echo 5. Press 'P' on any webpage to solve it
echo.
echo Keep this window open!
echo.
pause
