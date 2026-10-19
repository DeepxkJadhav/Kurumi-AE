@echo off
title Kurumi-AE Desktop Companion
cd /d "C:\REA\N.E.K.O"

echo ====================================================================
echo  [Kurumi-AE] Victorian Gothic 3D Desktop Companion (Zafkiel)
echo  Companion URL: http://127.0.0.1:48911
echo ====================================================================

:: Check if server is already running on port 48911
curl.exe -s -o nul http://127.0.0.1:48911/
if %ERRORLEVEL% equ 0 (
    echo [Kurumi-AE] Backend service is already active!
) else (
    echo [Kurumi-AE] Launching backend server...
    start "Kurumi Backend" /min "C:\Users\deepa\.local\bin\uv.exe" run python launcher.py
    echo [Kurumi-AE] Waiting for service initialization...
    timeout /t 6 /nobreak > nul
)

:: Launch standalone desktop application window
echo [Kurumi-AE] Summoning Desktop Companion Window...
if exist "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" (
    start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --app="http://127.0.0.1:48911/" --window-size=1280,850
) else if exist "C:\Program Files\Google\Chrome\Application\chrome.exe" (
    start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --app="http://127.0.0.1:48911/" --window-size=1280,850
) else (
    start "" "http://127.0.0.1:48911/"
)

exit /b 0
