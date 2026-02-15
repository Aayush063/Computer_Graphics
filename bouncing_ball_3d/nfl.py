import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import random

# 🔥 Fixed random pattern
random.seed(42)

# -------- Cube Data --------0

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0,1),(0,3),(0,4),
    (2,1),(2,3),(2,7),
    (6,3),(6,4),(6,7),
    (5,1),(5,4),(5,7)
)

# -------- Ball + Hole Properties --------
ball_radius = 0.2
hole_radius = 0.4
hole_z = 1

def reset_ball():
    global ball_x, ball_y, ball_z
    global vel_x, vel_y, vel_z
    global ball_exited, start_time

    ball_x = 0
    ball_y = 0
    ball_z = -0.5

    # 🔥 Random velocities (repeatable because of seed)
    vel_x = random.uniform(-0.02,0.02)
    vel_y = random.uniform(-0.02,0.02)
    vel_z = random.uniform(-0.02,0.02)

    ball_exited = False
    start_time = pygame.time.get_ticks()

reset_ball()

# -------- Draw Cube --------
def Cube():
    glColor3f(1,1,1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# -------- Draw Hole --------
def draw_hole():
    glColor3f(1,0,0)
    glBegin(GL_LINE_LOOP)
    for i in range(40):
        angle = i * 2 * math.pi / 40
        x = hole_radius * math.cos(angle)
        y = hole_radius * math.sin(angle)
        glVertex3f(x, y, hole_z)
    glEnd()

# -------- Draw Ball --------
def draw_ball():
    glPushMatrix()
    glTranslatef(ball_x, ball_y, ball_z)
    glColor3f(0,1,0)
    quad = gluNewQuadric()
    gluSphere(quad, ball_radius, 20, 20)
    glPopMatrix()

# -------- Update Physics --------
def update_ball():
    global ball_x, ball_y, ball_z
    global vel_x, vel_y, vel_z
    global ball_exited

    if ball_exited:
        ball_z += vel_z
        return

    ball_x += vel_x
    ball_y += vel_y
    ball_z += vel_z

    limit = 1 - ball_radius

    # Bounce X
    if ball_x > limit or ball_x < -limit:
        vel_x *= -1

    # Bounce Y
    if ball_y > limit or ball_y < -limit:
        vel_y *= -1

    # Back wall
    if ball_z < -limit:
        vel_z *= -1

    # Front wall (hole check)
    if ball_z > hole_z - ball_radius:
        distance = math.sqrt(ball_x**2 + ball_y**2)
        if distance < hole_radius:
            print("Ball exited through hole!")
            ball_exited = True
        else:
            vel_z *= -1

# -------- Random Rotation Setup --------
rot_x = random.uniform(-1, 1)
rot_y = random.uniform(-1, 1)
rot_z = random.uniform(-1, 1)

rotation_speed = random.uniform(0.3, 1.0)
angle = 0

# -------- Main --------
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

gluPerspective(45, display[0]/display[1], 0.1, 50.0)
glTranslatef(0, 0, -6)

glEnable(GL_DEPTH_TEST)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Reset after 30 seconds
    current_time = pygame.time.get_ticks()
    if current_time - start_time > 30000:
        reset_ball()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()

    # 🔥 Random continuous rotation
    angle += rotation_speed
    glRotatef(angle, rot_x, rot_y, rot_z)

    Cube()
    draw_hole()
    update_ball()
    draw_ball()

    glPopMatrix()

    pygame.display.flip()
    clock.tick(60)