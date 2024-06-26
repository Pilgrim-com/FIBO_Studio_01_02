import os
import sys
import pygame
from pygame.locals import *
import customtkinter as ctk
from customtkinter import *
from tkinter import *
from more import Variable, Title, next_page, back_page
import math


class Page3(ctk.CTkFrame):
    def __init__(self, parent, size):
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
        self.back_frame = Button(self, self.shoot_projectile)
        self.back_frame.grid(row=2, column=0, sticky='s', columnspan=3)

    def shoot_projectile(self):
        # Shoot a projectile from the left side of the screen towards the right
        self.simulation_frame.add_projectile()

class Projectile(pygame.sprite.Sprite):
    def __init__(self, u, theta):
        super().__init__()
        self.u = u
        self.theta = math.radians(abs(theta))
        self.x, self.y = Variable.ORIGIN
        self.color = Variable.BLACK

        # Calculate initial horizontal and vertical components of velocity
        self.vx = self.u * math.cos(self.theta) # ux = ucos
        self.vy = -self.u * math.sin(self.theta) # uy = usin
        self.time = 0 
        self.dt = 0.1 # Time step

        self.range_ = 765 # ระยะแกน x
        self.path = []

    def update(self):
        self.time += self.dt
        self.x = Variable.ORIGIN[0] + self.vx * self.time # x = x0 + uxt
        self.y = Variable.ORIGIN[1] + (self.vy * self.time + 0.5 * Variable.G * self.time ** 2) # y = y0 + uyt + 0.5gt^2

        if self.x >= self.range_:
            self.vx = 0
            self.vy = 0

        # Append new position to path
        self.path.append((self.x, self.y)) # เก็บค่าตำแหน่ง x,y ของลูก
        self.path = self.path[-50:]

        # Draw projectile
        pygame.draw.circle(self.screen, Variable.GREEN, (int(self.x), int(self.y)), 7) #color, position, radius
        pygame.draw.circle(self.screen, Variable.WHITE, (int(self.x), int(self.y)), 5, 1) #color, position, radius, width
        for pos in self.path[:-1:2]:
            pygame.draw.circle(self.screen, Variable.GREEN, (int(pos[0]), int(pos[1])), 1)

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

        # Load the image
        self.image = pygame.image.load('Side_view.png')
        # Resize the image
        new_size = (120, 90)  # Width, height
        self.resized_image = pygame.transform.scale(self.image, new_size)

        # Create the static elements
        self.target =  Rectangle(760, 263 - (Variable.position_y * 0.1 * 3) - 9.75, 10, 19.5, Variable.GREEN)
        self.target2 =  Rectangle(760, 263 - 145.5, 10, 145.5, Variable.RED)
        self.wall = Rectangle(460, 310, 10, 180, Variable.BLACK)
        self.base = Rectangle(760, 263, 10, 227, Variable.BLACK)
        self.floor = Rectangle(40, 490, 730, 10, Variable.BLACK)
        
        self.update_pygame()

    def init_pygame(self):
        # Set up the Pygame environment
        os.environ['SDL_WINDOWID'] = str(self.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'
        pygame.init()
        pygame.font.init()
        
        self.screen = pygame.display.set_mode((self.winfo_width(), self.winfo_height()))
        self.clock = pygame.time.Clock()

    def add_projectile(self):
        # Create target
        self.target =  Rectangle(760, 263 - (Variable.position_y * 0.1 * 3) - 9.75, 10, 19.5, Variable.GREEN)

        # Add a projectile at the specified position with initial velocities
        target_x, target_y = 765, 263 - (Variable.position_y * 0.1 * 3) 
        dx = target_x - Variable.ORIGIN[0]
        dy = Variable.ORIGIN[1] - target_y
        theta = 45
        theta_rad = math.radians(theta)

        # Calculate the necessary initial velocity (u) for the projectile to hit the target
        u = math.sqrt((-0.5 * Variable.G * dx * dx) / ((dy - dx * math.tan(theta_rad)) * (math.cos(theta_rad) ** 2)))
        self.projectiles.append(Projectile(u, theta))
        print((Variable.position_y * 0.1 * 3))

    def update_pygame(self):
        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                self.master.destroy()
                sys.exit()

        # Clear the screen with white color
        self.screen.fill(Variable.WHITE)

        # Move and draw each projectile
        for projectile in self.projectiles:
            projectile.screen = self.screen
            projectile.update()

        # Draw static elements
        self.wall.draw(self.screen)
        self.base.draw(self.screen)
        self.floor.draw(self.screen)
        self.target2.draw(self.screen)
        self.target.draw(self.screen)

        # Draw additional static graphics
        # pygame.draw.line(self.screen, BLACK, ORIGIN, (ORIGIN[0] + 100, ORIGIN[1]), 2)
        # pygame.draw.line(self.screen, BLACK, ORIGIN, (ORIGIN[0], ORIGIN[1] - 100), 2)
        # pygame.draw.circle(self.screen, BLACK, ORIGIN, 2)
        # pygame.draw.polygon(self.screen, Variable.BLACK, [(40, 490), (160, 490), (160, 400)])

        # Blit the image onto the screen at position (x, y)
        self.screen.blit(self.resized_image, (40, 400))

        font = pygame.font.SysFont('Arial', 30)
        # Render text to a surface
        wall = font.render('Wall', True, Variable.BLACK)
        target = font.render('Target', True, Variable.BLACK)
        self.screen.blit(wall, (440, 505))
        self.screen.blit(target, (740, 505))

        pygame.display.update()

        # Continue updating
        self.after(10, self.update_pygame)

class Button(Frame):
    def __init__(self, parent, projectile):
        super().__init__(parent, bg='#2B2B2B')
        next = next_page()
        back = back_page()
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
                                            command=next)
        self.button_back = ctk.CTkButton(self,
                                         text='Back',
                                         width=25, height=30,
                                         font=('Arial', 16),
                                         fg_color='#99B4DA',
                                         hover_color="#506988",
                                         text_color='black',
                                         corner_radius=10,
                                         command=back)

        # Layout
        self.button_sim.pack(side='right', padx=10, pady=10)
        self.button_restart.pack(side='right', padx=10, pady=10)
        self.button_back.pack(side='right', padx=10, pady=10)