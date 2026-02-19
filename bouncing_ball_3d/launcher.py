"""
Launcher for Color Shift Survival Game
Provides a simple GUI to start the game
"""
import tkinter as tk
from tkinter import ttk
import subprocess
import os
import sys

class GameLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Shift Survival - Launcher")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Center window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (self.root.winfo_width() // 2)
        y = (self.root.winfo_screenheight() // 2) - (self.root.winfo_height() // 2)
        self.root.geometry(f"+{x}+{y}")
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the launcher UI"""
        # Title
        title_label = tk.Label(
            self.root,
            text="Color Shift Survival",
            font=("Arial", 24, "bold"),
            fg="#2196F3"
        )
        title_label.pack(pady=20)
        
        # Subtitle
        subtitle_label = tk.Label(
            self.root,
            text="Match colors to survive!",
            font=("Arial", 12),
            fg="#666666"
        )
        subtitle_label.pack(pady=5)
        
        # Info frame
        info_frame = ttk.Frame(self.root)
        info_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        info_text = tk.Label(
            info_frame,
            text="Controls:\n"
                 "← → : Move the ball\n"
                 "SPACE : Change color\n"
                 "R : Restart game",
            font=("Arial", 10),
            justify="left",
            fg="#333333"
        )
        info_text.pack()
        
        # Button frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20, fill="x", padx=20)
        
        # Play button
        self.play_btn = ttk.Button(
            button_frame,
            text="Play Game",
            command=self.start_game
        )
        self.play_btn.pack(side="left", padx=5, expand=True, fill="x")
        
        # Exit button
        self.exit_btn = ttk.Button(
            button_frame,
            text="Exit",
            command=self.root.quit
        )
        self.exit_btn.pack(side="left", padx=5, expand=True, fill="x")
    
    def start_game(self):
        """Start the game"""
        try:
            self.play_btn.config(state="disabled")
            self.root.update()
            
            # Try to run the game
            if os.path.exists("project.py"):
                subprocess.Popen([sys.executable, "project.py"])
            else:
                # If running from dist folder
                import subprocess
                subprocess.Popen(os.path.join(os.path.dirname(__file__), "ColorShiftSurvival.exe"))
            
            self.root.destroy()
        except Exception as e:
            print(f"Error starting game: {e}")
            self.play_btn.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    launcher = GameLauncher(root)
    root.mainloop()
