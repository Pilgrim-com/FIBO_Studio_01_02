import os
import sys
import pygame
from pygame.locals import *
import customtkinter as ctk
from customtkinter import *
from tkinter import *
from more import Variable, Title

class Page3(ctk.CTkFrame):
    def __init__(self, parent, size, next_page, back_page):
        super().__init__(parent, width = size[0], height = size[1], bg_color = '#2B2B2B')

        # Define grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # Text Frame
        self.text_frame = Title(self, 'Simulation')
        self.text_frame.grid(row = 0, column = 0, sticky='n', columnspan=3)

        # Simulation
        self.simulation_frame = Simulation(self, width = 900, height = 550)
        self.simulation_frame.grid(row = 1, column = 0, columnspan=3)

        # Button Frame
        self.back_frame = Button(self, next_page, back_page, self.shoot_projectile)
        self.back_frame.grid(row = 2, column = 0, sticky='s', columnspan=3)

    def shoot_projectile(self):
            # Shoot a projectile from the left side of the screen towards the right
            x = 0
            y = self.simulation_frame.winfo_height() - 40  # Starting near the bottom
            self.simulation_frame.add_projectile(x, y)

class Projectile:
    def __init__(self, x, y, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.color = (0, 255, 0)  # Green color
        self.radius = 5
        self.gravity = 100 / 1000  # 10 pixels per second squared

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.velocity_y += self.gravity

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

class Simulation(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.init_pygame()
        self.projectiles = []
        self.update_pygame()

    def init_pygame(self):
        # Set up the Pygame environment
        os.environ['SDL_WINDOWID'] = str(self.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'
        pygame.init()
        
        self.screen = pygame.display.set_mode((self.master.winfo_width(), self.winfo_height()))
        self.clock = pygame.time.Clock()

    def add_projectile(self, x, y):
        # Add a projectile at the specified position with initial velocities
        initial_velocity_x = 5
        initial_velocity_y = -5  # Negative to move up initially
        self.projectiles.append(Projectile(x, y, initial_velocity_x, initial_velocity_y))

    def update_pygame(self):
        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                self.master.destroy()
                sys.exit()

        # Clear the screen with black color
        self.screen.fill((0, 0, 0))

        # Draw the floor
        Rectangle(0, self.winfo_height() - 10, self.winfo_width(), 10, self.screen)

        # Move and draw each projectile
        for projectile in self.projectiles:
            projectile.move()
            projectile.draw(self.screen)

        pygame.display.update()

        # Continue updating
        self.after(10, self.update_pygame)

class Button(Frame):
    def restart(self):
        self.next_page

        
    def __init__(self, parent, next_page, back_page, projectile):
        super().__init__(parent, bg = '#2B2B2B')
        self.next_page = next_page
        # Button
        self.button_sim = ctk.CTkButton(self,
                                    text = 'Simulation',
                                    width = 25, height = 30,
                                    font = ('Arial', 16),
                                    fg_color = '#99B4DA',
                                    hover_color = "#506988",
                                    text_color = 'black',
                                    corner_radius = 10,
                                    command = projectile)
        self.button_restart = ctk.CTkButton(self,
                                    text = 'Restart',
                                    width = 25, height = 30,
                                    font = ('Arial', 16),
                                    fg_color = '#99B4DA',
                                    hover_color = "#506988",
                                    text_color = 'black',
                                    corner_radius = 10,
                                    command = next_page)
        self.button_back = ctk.CTkButton(self,
                                    text = 'Back',
                                    width = 25, height = 30,
                                    font = ('Arial', 16),
                                    fg_color = '#99B4DA',
                                    hover_color = "#506988",
                                    text_color = 'black',
                                    corner_radius = 10,
                                    command = back_page)

        # Layout
        self.button_sim.pack(side='right', padx = 10, pady = 10)
        self.button_restart.pack(side='right', padx = 10, pady = 10)
        self.button_back.pack(side='right', padx = 10, pady = 10)