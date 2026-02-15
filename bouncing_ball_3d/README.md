# 3D Bouncing Ball (exit through a hole)

Simple Python demo showing a ball bouncing inside a cube and exiting through a rectangular hole on the +Z face.

Requirements
- Python 3.8+
- See `requirements.txt` (install with `pip install -r requirements.txt`).

Run

```powershell
python "bouncing_ball_3d\main.py"
```

Controls
- `R` : reset ball and simulation

Notes
- The project uses `pyglet` for windowing/OpenGL context and `PyOpenGL` to draw a sphere.
- The hole is highlighted with a red rectangle on the +Z face.
