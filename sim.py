import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN = WIDTH, HEIGHT = 900, 550
win = pygame.display.set_mode(SCREEN)
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Constants
origin = (160, 430)
g = 9.81

# Define projectile class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, u, theta):
        super().__init__()
        self.u = u
        self.theta = math.radians(abs(theta))
        self.x, self.y = origin
        self.color = BLACK

        # Calculate initial horizontal and vertical components of velocity
        self.vx = self.u * math.cos(self.theta)
        self.vy = -self.u * math.sin(self.theta)
        self.time = 0
        self.dt = 0.1  # time step

        self.range_ = 765
        self.path = []

    def update(self):
        self.time += self.dt
        self.x = origin[0]+  self.vx * self.time
        self.y = origin[1] + (self.vy * self.time + 0.5 * g * self.time ** 2)

        if self.x >= self.range_:
            self.vx = 0
            self.vy = 0

        # Append new position to path
        self.path.append((self.x, self.y))
        self.path = self.path[-50:]

        # Draw projectile
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), 5)
        pygame.draw.circle(win, WHITE, (int(self.x), int(self.y)), 5, 1)
        for pos in self.path[:-1:5]:
            pygame.draw.circle(win, WHITE, (int(pos[0]), int(pos[1])), 1)

# Define your rectangle class
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = BLACK

    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

def main():
    # Target coordinates
    target_x, target_y = 765, 263
    dx = target_x - origin[0]
    dy = origin[1] - target_y

    # Fixed angle (45 degrees in radians)
    theta = math.radians(45)

    # Calculate the necessary initial velocity (u) for the projectile to hit the target
    u = math.sqrt((dx * g) / math.sin(2 * theta))

    projectile = Projectile(u, 45)  # Initial velocity and fixed angle (45 degrees)
    wall = Rectangle(460, 310, 10, 180)  # Initial position and dimensions of the rectangle
    target = Rectangle(760, 263, 10, 227)  # Initial position and dimensions of the target rectangle
    floor = Rectangle(80, 490, 690, 10)  # Floor rectangle

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        win.fill(WHITE)

        # Update and draw projectile
        projectile.update()
        pygame.draw.line(win, BLACK, origin, (origin[0] + 100, origin[1]), 2)
        pygame.draw.line(win, BLACK, origin, (origin[0], origin[1] - 100), 2)
        pygame.draw.circle(win, BLACK, origin, 2)

        # Draw rectangles
        wall.draw()
        target.draw()
        floor.draw()

        # Draw triangle
        pygame.draw.polygon(win, BLACK, [(80, 490), (160, 490), (160, 430)])

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
