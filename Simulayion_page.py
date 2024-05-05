import tkinter as tk
import customtkinter as ctk
from tkinter import *
from more import Variable, Title

class Page3(ctk.CTkFrame):
    def __init__(self, parent, size, back_page):
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
        
        # Button Frame
        self.back_frame = Button(self, back_page)
        self.back_frame.grid(row = 2, column = 0, sticky='s', columnspan=3)

class Simulation(ctk.CTkFrame):
    def __init__(self):
        super().__init__()


class Button(tk.Frame):
    def __init__(self, parent, back_page):
        super().__init__(parent, bg = '#2B2B2B')

        # Button
        self.button_sim = ctk.CTkButton(self,
                                    text = 'Simulation',
                                    width = 25, height = 30,
                                    font = ('Arial', 16),
                                    fg_color = '#99B4DA',
                                    hover_color = "#506988",
                                    text_color = 'black',
                                    corner_radius = 10,
                                    command = Simulation)
        self.button_restart = ctk.CTkButton(self,
                                    text = 'Restart',
                                    width = 25, height = 30,
                                    font = ('Arial', 16),
                                    fg_color = '#99B4DA',
                                    hover_color = "#506988",
                                    text_color = 'black',
                                    corner_radius = 10)
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