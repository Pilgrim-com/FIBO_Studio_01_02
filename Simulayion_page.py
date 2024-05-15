import os
import sys
import pygame
from pygame.locals import *
import customtkinter as ctk
from customtkinter import *
from tkinter import *
from more import Variable, Title
import math

# Constants for the simulation
SCREEN = WIDTH, HEIGHT = 900, 550
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
ORIGIN = (160, 400)
G = 9.81

class Page3(ctk.CTkFrame):
    def __init__(self, parent, size, next_page, back_page):
        super().__init__(parent, width=size[0], height=size[1], bg_color='#2B2B2B')

        # Define grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # Text Frame
        self.text_frame = Title(self, 'Simulation')
        self.text_frame.grid(row=0, column=0, sticky='n', columnspan=3)

        # Simulation
        self.simulation_frame = Simulation(self, width=850, height=550)
        self.simulation_frame.grid(row=1, column=0, columnspan=3)

        # Button Frame
        self.back_frame = Button(self, next_page, back_page, self.shoot_projectile)
        self.back_frame.grid(row=2, column=0, sticky='s', columnspan=3)

    def shoot_projectile(self):
        # Shoot a projectile from the left side of the screen towards the right
        x = 160
        y = 400  # Starting near the bottom
        self.simulation_frame.add_projectile(x, y)

# Define projectile class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, u, theta):
        super().__init__()
        self.u = u
        self.theta = math.radians(abs(theta))
        self.x, self.y = ORIGIN
        self.color = BLACK

        # Calculate initial horizontal and vertical components of velocity
        self.vx = self.u * math.cos(self.theta)
        self.vy = -self.u * math.sin(self.theta)
        self.time = 0
        self.dt = 0.1 # Time step

        self.range_ = 765
        self.path = []

    def update(self):
        self.time += self.dt
        self.x = ORIGIN[0] + self.vx * self.time
        self.y = ORIGIN[1] + (self.vy * self.time + 0.5 * G * self.time ** 2)

        if self.x >= self.range_:
            self.vx = 0
            self.vy = 0

        # Append new position to path
        self.path.append((self.x, self.y))
        self.path = self.path[-50:]

        # Draw projectile
        pygame.draw.circle(self.screen, GREEN, (int(self.x), int(self.y)), 7) #color, position, radius
        pygame.draw.circle(self.screen, WHITE, (int(self.x), int(self.y)), 5, 1) #color, position, radius, width
        for pos in self.path[:-1:2]:
            pygame.draw.circle(self.screen, GREEN, (int(pos[0]), int(pos[1])), 1)

# Define your rectangle class
class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class Simulation(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.init_pygame()
        self.projectiles = []

        # Create the static elements
        self.wall = Rectangle(460, 310, 10, 180, BLACK)
        self.target = Rectangle(760, 263 - 60, 10, 19.5, GREEN)
        self.base = Rectangle(760, 263, 10, 227, BLACK)
        self.floor = Rectangle(40, 490, 730, 10, BLACK)
        
        self.update_pygame()

    def init_pygame(self):
        # Set up the Pygame environment
        os.environ['SDL_WINDOWID'] = str(self.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'
        pygame.init()
        
        self.screen = pygame.display.set_mode((self.winfo_width(), self.winfo_height()))
        self.clock = pygame.time.Clock()

    def add_projectile(self, x, y):
        # Add a projectile at the specified position with initial velocities
        # Calculate the necessary initial velocity (u) for the projectile to hit the target
        target_x, target_y = 765, 263 - 60#max 91.5 = 30.5 * 3
        dx = target_x - ORIGIN[0]
        dy = ORIGIN[1] - target_y
        theta = 45
        theta_rad = math.radians(theta)
        u = math.sqrt((-0.5 * G * dx * dx) / ((dy - dx * math.tan(theta_rad)) * (math.cos(theta_rad) ** 2)))
        self.projectiles.append(Projectile(u, theta))

    def update_pygame(self):
        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                self.master.destroy()
                sys.exit()

        # Clear the screen with white color
        self.screen.fill(WHITE)

        # Move and draw each projectile
        for projectile in self.projectiles:
            projectile.screen = self.screen
            projectile.update()

        # Draw static elements
        self.wall.draw(self.screen)
        self.target.draw(self.screen)
        self.base.draw(self.screen)
        self.floor.draw(self.screen)

        # Draw additional static graphics
        """ pygame.draw.line(self.screen, BLACK, ORIGIN, (ORIGIN[0] + 100, ORIGIN[1]), 2)
        pygame.draw.line(self.screen, BLACK, ORIGIN, (ORIGIN[0], ORIGIN[1] - 100), 2)
        pygame.draw.circle(self.screen, BLACK, ORIGIN, 2) """
        pygame.draw.polygon(self.screen, BLACK, [(40, 490), (160, 490), (160, 400)])

        pygame.display.update()

        # Continue updating
        self.after(10, self.update_pygame)

class Button(Frame):
    def restart(self):
        self.next_page

    def __init__(self, parent, next_page, back_page, projectile):
        super().__init__(parent, bg='#2B2B2B')
        self.next_page = next_page
        # Button
        self.button_sim = ctk.CTkButton(self,
                                        text='Simulation',
                                        width=25, height=30,
                                        font=('Arial', 16),
                                        fg_color='#99B4DA',
                                        hover_color="#506988",
                                        text_color='black',
                                        corner_radius=10,
                                        command=projectile)
        self.button_restart = ctk.CTkButton(self,
                                            text='Restart',
                                            width=25, height=30,
                                            font=('Arial', 16),
                                            fg_color='#99B4DA',
                                            hover_color="#506988",
                                            text_color='black',
                                            corner_radius=10,
                                            command=next_page)
        self.button_back = ctk.CTkButton(self,
                                         text='Back',
                                         width=25, height=30,
                                         font=('Arial', 16),
                                         fg_color='#99B4DA',
                                         hover_color="#506988",
                                         text_color='black',
                                         corner_radius=10,
                                         command=back_page)

        # Layout
        self.button_sim.pack(side='right', padx=10, pady=10)
        self.button_restart.pack(side='right', padx=10, pady=10)
        self.button_back.pack(side='right', padx=10, pady=10)
