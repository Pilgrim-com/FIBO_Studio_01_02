import customtkinter as ctk
from tkinter import *

class Variable:
    position_x = 0
    position_y = 0
    velocity_start = -1
    rpm = 0
    voltage = 0
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    ORIGIN = (160, 400)
    G = 9.81
    current_page = 0
    pages = []

class Title(Frame):
    def __init__(self, parent, title):
        super().__init__(parent, bg = '#2C2C2C')
        self.label = ctk.CTkLabel(self, text = title, font = ('Interb', 32), bg_color = '#2C2C2C')
        self.label.pack(pady = (15, 0))
        
class next_page:
    def __call__(self):
        if Variable.pages:  # Check if Variable.pages is not empty
            Variable.pages[Variable.current_page].pack_forget()  # Hide current page
            Variable.current_page = (Variable.current_page + 1) % len(Variable.pages)  # Move to next page
            Variable.pages[Variable.current_page].pack(fill='both', expand=True)  # Show next page

class back_page:
    def __call__(self):
        if Variable.pages:  # Check if Variable.pages is not empty
            Variable.pages[Variable.current_page].pack_forget()  # Hide current page
            Variable.current_page = (Variable.current_page - 1) % len(Variable.pages)  # Move to previous page
            Variable.pages[Variable.current_page].pack(fill='both', expand=True)  # Show previous page
