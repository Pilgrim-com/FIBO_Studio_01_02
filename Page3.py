import tkinter as tk
from tkinter import *

""" class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])

        Page3_size = (size[0], size[1])
        Page3(self, Page3_size).pack()

        self.mainloop() """

class Page3(tk.Frame):
    def __init__(self, parent, size, b_back):
        super().__init__(parent)
        self.config(width = size[0], height = size[1])

        # Define grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # Text Frame
        self.text_frame = Title(self)
        self.text_frame.grid(row = 0, column = 0, sticky='n', columnspan=3)

        # Button Frame
        self.back_frame = Button(self, b_back)
        self.back_frame.grid(row = 2, column = 0, sticky='s', columnspan=3)

class Title(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text=" Simulation ", font="Inter 32 bold")
        self.label.pack()
        #self.label.place(relx=0.5, rely=0.03, anchor='center')

class Calculate():
    def __init__(self, parent):
        super().__init__(parent)

class Simulation(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)

class Button(tk.Frame):
    def __init__(self, parent, b_back):
        super().__init__(parent)

        # Button
        self.button_sim = tk.Button(self, text='Simulation', command = Simulation)
        self.button_restart = tk.Button(self, text='Restart')
        self.button_back = tk.Button(self, text='Back', command = b_back)

        # Layout
        self.button_sim.pack(side='right', padx=5, pady=5)
        self.button_restart.pack(side='right', padx=5, pady=5)
        self.button_back.pack(side='right', padx=5, pady=5)

""" # Create and run the app
app = App('Simulation', (850, 600)) """