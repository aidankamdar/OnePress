# Chrome Launcher with Remote Debugging
# Run this in PowerShell as Administrator

Write-Host ""
Write-Host "============================================================" -ForegroundColor Green
Write-Host "Chrome Launcher with Remote Debugging" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host ""

# Close any existing Chrome processes
Write-Host "Closing any running Chrome processes..." -ForegroundColor Yellow
Stop-Process -Name chrome -Force -ErrorAction SilentlyContinue
Start-Sleep -Seconds 2

# Find Chrome
$chromePaths = @(
    "C:\Program Files\Google\Chrome\Application\chrome.exe",
    "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe"
)

$chromePath = $null
foreach ($path in $chromePaths) {
    if (Test-Path $path) {
        $chromePath = $path
        break
    }
}

if (-not $chromePath) {
    Write-Host "ERROR: Chrome not found!" -ForegroundColor Red
    pause
    exit
}

Write-Host "Found Chrome at: $chromePath" -ForegroundColor Cyan
Write-Host ""

# Launch Chrome with debugging
Write-Host "Launching Chrome with debugging on port 9222..." -ForegroundColor Yellow
$profilePath = "$env:TEMP\chrome-debug-profile"
Start-Process -FilePath $chromePath -ArgumentList "--remote-debugging-port=9222", "--user-data-dir=$profilePath"

Start-Sleep -Seconds 2

Write-Host ""
Write-Host "============================================================" -ForegroundColor Green
Write-Host "SUCCESS! Chrome is running with debugging enabled" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host ""
Write-Host "NEXT STEPS:" -ForegroundColor Yellow
Write-Host "1. Browse to any webpage with a problem"
Write-Host "2. In THIS PowerShell window, run: python onepress.py"
Write-Host "3. Press 'P' on any webpage to get solutions"
Write-Host ""
Write-Host "Chrome is now ready!" -ForegroundColor Green
Write-Host ""

