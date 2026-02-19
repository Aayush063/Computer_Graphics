# Color Shift Survival - Installation Guide

## Overview
This guide will help you create a Windows installer for the Color Shift Survival game.

## Prerequisites
- Windows 10/11
- Python 3.8+ installed (https://www.python.org)
- Administrator access (recommended)

## Installation Steps

### Option 1: Quick Install (Recommended)
1. Double-click `install.bat`
2. Wait for the installation to complete
3. Find `ColorShiftSurvival.exe` in the `dist` folder
4. Create a shortcut to your Desktop for easy access

### Option 2: Manual Install
1. Open PowerShell or Command Prompt in this folder
2. Run: `pip install -r requirements.txt`
3. Run: `python build_installer.py`
4. Find `ColorShiftSurvival.exe` in the `dist` folder

## Creating a Desktop Shortcut

1. Navigate to `dist` folder
2. Right-click `ColorShiftSurvival.exe`
3. Select "Create shortcut"
4. Move the shortcut to your Desktop

## Running the Game

### With Launcher (GUI)
```powershell
python launcher.py
```

### Direct Executable
```powershell
dist/ColorShiftSurvival.exe
```

## Game Controls
- **← →** : Move the ball left/right
- **SPACE** : Change ball color
- **R** : Restart after game over

## Troubleshooting

### "Python is not installed"
- Install Python from https://www.python.org
- Make sure to check "Add Python to PATH" during installation

### "pygame module not found"
- Run: `pip install pygame`

### Executable won't run
- Install all dependencies: `pip install -r requirements.txt`
- Rebuild: `python build_installer.py`

## Features
- Single EXE file (no dependencies needed after building)
- High score tracking
- Progressive difficulty
- Color-matching gameplay

## Creating an Installer with NSIS (Advanced)

For a professional installer (.msi/.exe setup):
1. Install NSIS from https://nsis.sourceforge.io
2. Use the `ColorShiftSurvival.exe` from the `dist` folder
3. Create an NSIS script to bundle and install

## Support
For issues, check that:
- Python is properly installed and in PATH
- All dependencies are installed: `pip install -r requirements.txt`
- The `highscore.txt` file exists in the same directory

Enjoy the game!
