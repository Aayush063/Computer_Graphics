import pygame
import random
import math
import sys

pygame.init()


# WINDOW SETUP

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Shift Survival - Final Version")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 28)
big_font = pygame.font.SysFont("arial", 60)


# HIGH SCORE SYSTEM

def load_high_score():
    try:
        with open("highscore.txt", "r") as file:
            return int(file.read())
    except:
        return 0

def save_high_score(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))

high_score = load_high_score()
new_high = False

# -----------------------
# COLORS
# -----------------------
COLORS = [
    (255, 80, 80),
    (80, 255, 120),
    (80, 150, 255),
    (255, 220, 70)
]

# -----------------------
# PLAYER CLASS
# -----------------------
class Player:
    def __init__(self):
        self.radius = 20
        self.x = WIDTH // 2
        self.y = HEIGHT - 120
        self.color_index = 0
        self.lives = 3
        self.speed = 6

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x - self.radius > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.radius < WIDTH:
            self.x += self.speed

    def switch_color(self):
        self.color_index = (self.color_index + 1) % len(COLORS)

    def draw(self):
        color = COLORS[self.color_index]
        pygame.draw.circle(screen, color, (int(self.x), self.y), self.radius)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), self.y), self.radius, 2)

# -----------------------
# OBSTACLE CLASS
# -----------------------
class Obstacle:
    def __init__(self, difficulty):
        self.radius = random.randint(70, 100)
        self.x = random.randint(150, WIDTH - 150)
        self.y = -100
        self.speed = 4 + difficulty
        self.rotation = 0
        self.rotation_speed = random.uniform(0.01, 0.03)
        self.colors = random.sample(COLORS, 4)
        self.checked = False

    def move(self):
        self.y += self.speed
        self.rotation += self.rotation_speed

    def draw(self):
        for i in range(4):
            start_angle = self.rotation + i * math.pi/2
            end_angle = start_angle + math.pi/2
            pygame.draw.arc(
                screen,
                self.colors[i],
                (self.x - self.radius, self.y - self.radius,
                 self.radius * 2, self.radius * 2),
                start_angle,
                end_angle,
                18
            )

    def check_collision(self, player):
        distance = math.hypot(player.x - self.x, player.y - self.y)

        if not self.checked and distance <= self.radius:
            self.checked = True

            angle = math.atan2(player.y - self.y, player.x - self.x)
            if angle < 0:
                angle += 2 * math.pi

            angle -= self.rotation
            if angle < 0:
                angle += 2 * math.pi

            segment = int(angle // (math.pi/2))

            if self.colors[segment] == COLORS[player.color_index]:
                return "score"
            else:
                return "hit"

        return None

# -----------------------
# BACKGROUND ANIMATION
# -----------------------
def draw_background(tick):
    for y in range(HEIGHT):
        r = int(40 + 40 * math.sin(tick * 0.02 + y * 0.01))
        g = int(40 + 40 * math.sin(tick * 0.02 + y * 0.015))
        b = int(80 + 40 * math.sin(tick * 0.02))
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

# -----------------------
# GAME VARIABLES
# -----------------------
player = Player()
obstacles = []
score = 0
difficulty = 0
spawn_timer = 0
tick = 0
game_over = False

# -----------------------
# MAIN GAME LOOP
# -----------------------
while True:
    clock.tick(60)
    tick += 1
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_SPACE:
                    player.switch_color()
            else:
                if event.key == pygame.K_r:
                    player = Player()
                    obstacles.clear()
                    score = 0
                    difficulty = 0
                    game_over = False
                    new_high = False

    draw_background(tick)

    if not game_over:

        player.move(keys)

        spawn_timer += 1
        if spawn_timer > 80:
            obstacles.append(Obstacle(difficulty))
            spawn_timer = 0

        for obstacle in obstacles[:]:
            obstacle.move()
            obstacle.draw()

            result = obstacle.check_collision(player)

            if result == "hit":
                player.lives -= 1
                obstacles.remove(obstacle)

            elif result == "score":
                score += 10
                difficulty += 0.2

            if obstacle.y > HEIGHT + 100:
                obstacles.remove(obstacle)

        player.draw()

        # UI
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        lives_text = font.render(f"Lives: {player.lives}", True, (255, 255, 255))
        high_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))

        screen.blit(score_text, (20, 20))
        screen.blit(lives_text, (20, 60))
        screen.blit(high_text, (20, 100))

        if player.lives <= 0:
            game_over = True

            if score > high_score:
                high_score = score
                save_high_score(high_score)
                new_high = True
            else:
                new_high = False

    else:
        over_text = big_font.render("GAME OVER", True, (255, 80, 80))
        final_score = font.render(f"Final Score: {score}", True, (255, 255, 255))
        high_display = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        restart_text = font.render("Press R to Restart", True, (255, 255, 255))

        screen.blit(over_text, (WIDTH//2 - over_text.get_width()//2, HEIGHT//2 - 120))
        screen.blit(final_score, (WIDTH//2 - final_score.get_width()//2, HEIGHT//2 - 40))
        screen.blit(high_display, (WIDTH//2 - high_display.get_width()//2, HEIGHT//2))
        screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 60))

        if new_high:
            new_text = font.render("NEW HIGH SCORE!", True, (255, 215, 0))
            screen.blit(new_text, (WIDTH//2 - new_text.get_width()//2, HEIGHT//2 + 100))

    pygame.display.flip()
