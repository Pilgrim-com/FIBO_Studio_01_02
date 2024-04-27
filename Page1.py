import tkinter as tk
from tkinter import *

class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])

        Page1_size = (size[0], size[1])
        Page1(self, Page1_size).pack()

        self.mainloop()

class Page1(tk.Frame):
    def __init__(self, parent, size):
        super().__init__(parent)
        self.config(width = size[0], height = size[1])
        # Define grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # Text
        self.text_frame = Title(self)
        self.text_frame.grid(row = 0, column = 0, sticky='n', columnspan=3)

        # Canvases
        self.canvas_frame = Canvas(self)
        self.canvas_frame.grid(row = 1, column = 0, sticky='we')

        # Input
        self.input_frame = Input(self)
        self.input_frame.grid(row = 1, column = 2, sticky='we')

        # Back
        self.back_frame = Button(self)
        self.back_frame.grid(row = 2, column = 0, sticky='news', columnspan=3)

class Title(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="Select Target Position", font="Inter 32 bold")
        self.label.pack()
        #self.label.place(relx=0.5, rely=0.03, anchor='center')

class Canvas(tk.Frame):
    def draw_triangle(self, canvas):
        # Clear canvas
        canvas.delete("all")

        # Define coordinates for the triangle
        x0, y0 = 50, 314.4  # Left point
        x1, y1 = 350, 314.4  # Right point
        x2, y2 = 200, 50  # Top point
        
        # Draw triangle
        canvas.create_polygon(x0, y0, x1, y1, x2, y2, fill="blue")

    def __init__(self, parent):
        super().__init__(parent)
        
        # Create and place canvas for triangle
        self.canvas = tk.Canvas(self, width=400, height=364.4)
        self.canvas.pack()

        # Draw triangle on canvas
        self.draw_triangle(self.canvas)

class Input(tk.LabelFrame):
    def Position(self):
        position_x = self.box1.get()
        print(position_x)
        position_y = self.box2.get()
        print(position_y)

    def __init__(self, parent):
        super().__init__(parent, text = ' Position ')
        
        # Create label and text box widgets
        self.label_x = tk.Label(self, text=" Posiotion x : ")
        self.label_y = tk.Label(self, text=" Posiotion y : ")
        
        # Create entry and button widgets
        self.entry_x = tk.Entry(self)
        self.entry_y = tk.Entry(self)

        #Button
        self.Add_button = tk.Button(self, text="Add position", command=self.Position)
        
        # Place label, text box, entry, button, and another text widgets using grid layout
        self.label_x.grid(row=0, column=0, sticky="w", padx=(10, 5), pady=(10, 5))
        self.entry_x.grid(row=1, column=0, padx=(10, 5), pady=(0, 5), sticky="w")
        self.label_y.grid(row=2, column=0, sticky="w", padx=(10, 5), pady=(10, 5))
        self.entry_y.grid(row=3, column=0, padx=(10, 5), pady=(0, 5), sticky="w")
        self.Add_button.grid(row=4, column=0, padx=(0, 10), pady=(0, 5), sticky="e")

class Button(tk.Frame):
    def Back():
        back = 1

    def __init__(self, parent):
        super().__init__(parent)

        self.button = tk.Button(self, text='Back', command=self.Back)
        self.button.pack(side = 'right')

# Create and run the app
app = App('Simulation', (850, 600))
