"""
Build script to create a Windows installer for Color Shift Survival
This script uses PyInstaller to create a standalone executable
"""
import os
import sys
import shutil
import subprocess

def build_executable():
    """Build the executable using PyInstaller"""
    print("=" * 60)
    print("Building Color Shift Survival Executable...")
    print("=" * 60)
    
    # Clean previous builds
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")
    
    # PyInstaller command
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",
        "--windowed",
        "--icon=NONE",
        "--add-data=highscore.txt:.",
        "--name=ColorShiftSurvival",
        "project.py"
    ]
    
    try:
        result = subprocess.run(cmd, check=True)
        print("\n" + "=" * 60)
        print("✓ Executable built successfully!")
        print("=" * 60)
        print(f"\nFind your executable at: {os.path.abspath('dist/ColorShiftSurvival.exe')}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Error building executable: {e}")
        return False

if __name__ == "__main__":
    build_executable()
