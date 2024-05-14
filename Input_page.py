import tkinter as tk
import customtkinter as ctk
from tkinter import *
from more import Variable, Title


class Page1(ctk.CTkFrame):
    def __init__(self, parent, size, next_page):
        super().__init__(parent, width = size[0], height = size[1], bg_color = '#2C2C2C')

        # Define grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # Text
        self.text_frame = Title(self, "Select Target Position")
        self.text_frame.grid(row = 0, column = 0, sticky='n', columnspan=3)

        # Canvases
        self.canvas_frame = Canvas(self)
        self.canvas_frame.grid(row = 1, column = 0, sticky='e')

        # Input
        self.input_frame = Input(self)
        self.input_frame.grid(row = 1, column = 2, sticky='w')

        # Back
        self.back_frame = Button(self, next_page)
        self.back_frame.grid(row = 2, column = 0, sticky='s', columnspan = 3)

class Canvas(ctk.CTkFrame):
    def draw_triangle(self, canvas):
        # Clear canvas
        canvas.delete("all")

        # Define coordinates for the triangle
        x0, y0 = 50, 314.4  # Left point
        x1, y1 = 350, 314.4  # Right point
        x2, y2 = 200, 50  # Top point
        
        # Draw triangle
        canvas.create_polygon(x0, y0, x1, y1, x2, y2, fill = "#506988")

    def draw_circle(self, canvas):
        # Define coordinate for the circle centered at (200, 182.2) with a radius of 50
        x0, y0 = 150, 132.2
        x1, y1 = 250, 232.2

        # Draw circle
        canvas.create_oval(x0, y0, x1, y1, fill = 'white')

    def draw_line(self, canvas):
        # Define coordinates for the line x
        x_x0, x_y0 = 0, 182.2
        x_x1, x_y1 = 400, 182.2 

        # Define coordinates for the line x
        y_x0, y_y0 = 200, 0
        y_x1, y_y1 = 200, 364.4 

        # Draw line
        canvas.create_line(x_x0, x_y0, x_x1, x_y1, width = 3, fill="#96A5C3")
        canvas.create_line(y_x0, y_y0, y_x1, y_y1, width = 3, fill="#A4574F")

    def __init__(self, parent):
        super().__init__(parent, width = 425, height = 300, bg_color = '#2C2C2C')
        
        # Create and place canvas for triangle
        self.canvas = tk.Canvas(self, width=400, height=364.4, bg = '#2C2C2C')

        # Draw on canvas
        self.draw_triangle(self.canvas)
        self.draw_circle(self.canvas)
        self.draw_line(self.canvas)
        self.canvas.create_text( 393, 165, text = 'x', font = ('Arial', 20), fill = "#96A5C3")
        self.canvas.create_text( 213.2, 350.4, text = 'y', font = ('Arial', 20), fill = "#A4574F")

        # Layout
        self.canvas.pack()

class Input(ctk.CTkFrame):
    def Calculate(self):

        self.Position()
        self.Velocity()
        self.RPM()
        self.Moter_voltage()
    
    def Position(self):
        Variable.position_x = int(self.entry_x.get())
        Variable.position_y = int(self.entry_y.get())
        print(Variable.position_x, Variable.position_y)

    def Velocity(self):
        Variable.velocity_start = int(Variable.position_x) * int(Variable.position_y)
        print(Variable.velocity_start)

    def RPM(self):
        Variable.rpm = int(Variable.velocity_start) * 2
        print(Variable.rpm)

    def Moter_voltage(self):
        Variable.voltage = int(Variable.rpm) * 2
        print(Variable.voltage)
    
    def delete(self):
        # Clear entry
        self.entry_x.delete(0, 'end')
        self.entry_y.delete(0, 'end')

        # Clear variable
        Variable.position_x = 0
        Variable.position_y = 0
        Variable.velocity_start = 0
        Variable.rpm = 0
        Variable.voltage = 0
        
    def __init__(self, parent):
        super().__init__(parent, width = 425, height = 300, bg_color = '#2B2B2B')

        # Create label and text box widgets
        self.label_x = ctk.CTkLabel(self, text="Target Posiotion x : ", font = ('Arial', 20))
        self.label_y = ctk.CTkLabel(self, text="Target Posiotion y : ", font = ('Arial', 20))
        
        # Create entry and button widgets
        self.entry_x = ctk.CTkEntry(self, placeholder_text = 'Enter x position of target (mm)', width = 210, height = 30, corner_radius = 10)
        self.entry_y = ctk.CTkEntry(self, placeholder_text = 'Enter y position of target (mm)', width = 210, height = 30, corner_radius = 10)

        #Button
        self.Add_button = ctk.CTkButton(self,
                                        text="Add position",
                                        width = 10, height = 10,
                                        font = ('Arial', 12),
                                        fg_color = '#99B4DA',
                                        hover_color = "#506988",
                                        text_color = 'black',
                                        command = self.Calculate)
        self.Re_button = ctk.CTkButton(self,
                                        text="Reset position",
                                        width = 10, height = 10,
                                        font = ('Arial', 12),
                                        fg_color = '#99B4DA',
                                        hover_color = "#506988",
                                        text_color = 'black',
                                        command = self.delete)
        
        # Place label, text box, entry, button, and another text widgets using grid layout
        self.label_x.grid(row=0, column=0, padx=20, pady = (20,0), sticky="w")
        self.entry_x.grid(row=1, column=0, padx=20, pady=(5, 15), sticky="w")
        self.label_y.grid(row=2, column=0, padx=20, sticky="w")
        self.entry_y.grid(row=3, column=0, padx=20, pady=5, sticky="w")
        self.Re_button.grid(row=4, column=0, padx=20, pady=(10, 20), sticky="w")
        self.Add_button.grid(row=4, column=0, padx=20, pady=(10, 20), sticky="e")

class Button(Frame):
    def __init__(self, parent, next_page):
        super().__init__(parent, bg = '#2B2B2B')

        self.button = ctk.CTkButton(self,
                                    text = 'Calculate',
                                    width = 25, height = 30,
                                    font = ('Arial', 16),
                                    fg_color = '#99B4DA',
                                    hover_color = "#506988",
                                    text_color = 'black',
                                    corner_radius = 10,
                                    command = next_page)
        self.button.pack(side = 'bottom', pady = (0, 10))