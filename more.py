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

class Title(ctk.CTkFrame):
    def __init__(self, parent, title):
        super().__init__(parent, bg_color = '#2C2C2C')
        self.label = ctk.CTkLabel(self, text = title, font = ('Inter', 32), bg_color = '#2C2C2C')
        self.label.pack()
        