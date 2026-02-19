@echo off
echo ============================================
echo Color Shift Survival - Installation
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org
    pause
    exit /b 1
)

echo Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Building executable...
python build_installer.py

if errorlevel 1 (
    echo Error: Failed to build executable
    pause
    exit /b 1
)

echo.
echo ============================================
echo Installation Complete!
echo ============================================
echo.
echo Your game is ready to play!
echo Run: ColorShiftSurvival.exe in the dist folder
echo.
pause
