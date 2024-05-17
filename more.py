import customtkinter as ctk
from tkinter import *

class Variable:
    position_x = -1
    position_y = -1
    velocity_start = -1
    rpm = -1
    voltage = -1
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    ORIGIN = (160, 400)
    G = 9.81

class canvas(Frame):
    def __init__(self, parent, width, height, bg):
        super().__init__(parent, bg = '#FFFFFF')
        
        # Create and place canvas for triangle
        self.canvas = Canvas(parent, width = width, height = height, bg = bg)

class Title(Frame):
    def __init__(self, parent, title):
        super().__init__(parent, bg = '#2C2C2C')
        self.label = ctk.CTkLabel(self, text = title, font = ('Interb', 32), bg_color = '#2C2C2C')
        self.label.pack(pady = (15, 0))
        