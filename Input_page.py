import math
import tkinter as tk
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from more import Variable, Title, next_page


class Page1(ctk.CTkFrame):
    def __init__(self, parent, size):
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
        self.input_frame = Input(self, canvas_frame = self.canvas_frame)
        self.input_frame.grid(row = 1, column = 2, sticky='w')

        # Button
        self.back_frame = Button(self)
        self.back_frame.grid(row = 2, column = 0, sticky='s', columnspan = 3)

class Canvas(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width = 425, height = 300, bg_color = '#2C2C2C')
        
        # Create and place canvas for triangle
        self.canvas = tk.Canvas(self, width=400, height=364.4, bg = '#FFFFFF')

        # Draw on canvas
        self.draw_triangle(self.canvas)
        self.draw_line(self.canvas)

        # Layout
        self.canvas.pack()

    def draw_triangle(self, canvas):
        # Declare coordinates for the triangle
        x0, y0 = 50, 314.4  # Left point
        x1, y1 = 350, 314.4  # Right point
        x2, y2 = 200, 50  # Top point
        
        # Draw triangle
        canvas.create_polygon(x0, y0, x1, y1, x2, y2, fill = "#506988")

    def draw_circle(self, canvas):
        # Define coordinate for the circle centered at (200, 182.2) with a radius of 50
        x0, y0 = 14.9 + (Variable.position_x * 0.54), 279.3 - (Variable.position_y * 0.545)
        x1, y1 = 85.1 + (Variable.position_x * 0.54), 349.5 - (Variable.position_y * 0.545)

        # Draw circle
        canvas.create_oval(x0, y0, x1, y1, fill = 'white') 

    def draw_line(self, canvas):
        # Define coordinates for the line x
        x_x0, x_y0 = 0, 314.4 - (Variable.position_y * 0.545)
        x_x1, x_y1 = 400, 314.4 - (Variable.position_y * 0.545)

        # Define coordinates for the line y
        y_x0, y_y0 = 50 + (Variable.position_x * 0.54), 0
        y_x1, y_y1 = 50 + (Variable.position_x * 0.54), 364.4 

        # Draw line
        canvas.create_line(x_x0, x_y0, x_x1, x_y1, width = 3, fill="#96A5C3")
        canvas.create_line(y_x0, y_y0, y_x1, y_y1, width = 3, fill="#A4574F")
        self.canvas.create_text( 393, (314.4 - 15) - ((Variable.position_y) * 0.545), text = 'x', font = ('Arial', 20), fill = "#96A5C3")
        self.canvas.create_text( 50 + ((Variable.position_x + 20) * 0.54), 10, text = 'y', font = ('Arial', 20), fill = "#A4574F")
        self.canvas.create_text( (50 + (Variable.position_x * 0.54)) + 55, (314.4 + 40) , text = f"({Variable.position_x}, {Variable.position_y})", font = ('Arial', 16), fill = "black")

    def update_canvas(self):
        self.canvas.delete("all")
        self.draw_triangle(self.canvas)
        if Variable.position_x != 0 and Variable.position_y != 0:
            self.draw_circle(self.canvas)
        self.draw_line(self.canvas)

class Input(ctk.CTkFrame):
    def __init__(self, parent, canvas_frame):
        super().__init__(parent, width = 425, height = 300, bg_color = '#2B2B2B')

        self.camvas_frame = canvas_frame

        # Create label and text box widgets
        self.label_x = ctk.CTkLabel(self, text="Target Position x : ", font = ('Arial', 20))
        self.label_y = ctk.CTkLabel(self, text="Target Position y : ", font = ('Arial', 20))
        
        # Create entry and button widgets
        self.entry_x = ctk.CTkEntry(self, placeholder_text = 'Enter x position 150 - 390 (mm)', width = 210, height = 30, corner_radius = 10)
        self.entry_y = ctk.CTkEntry(self, placeholder_text = 'Enter y position 83 - 305 (mm)', width = 210, height = 30, corner_radius = 10)

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

    def Calculate(self):
        x = int(self.entry_x.get())
        Variable.position_y = int(self.entry_y.get())
        Variable.position_x = x
        
        print(Variable.position_x, Variable.position_y)
        if (Variable.position_x < 150 or Variable.position_x > 390) or (Variable.position_y < 83 or Variable.position_y > 305):
            messagebox.showerror("Error", 'Please enter the correct value of targrt position x and y')
        else:
            self.camvas_frame.updeted_canvas()
            self.Velocity()
            self.RPM()
            self.Moter_voltage()
            
    def Velocity(self):
        g = 9.81
        h = 0.755 + (Variable.position_y * 0.001) # ระยะในแกน y
        u = (4*(-g))/(h-2) # คำนวณความเร็วต้นของลูกสควอชจากสูตร projectile
        Variable.velocity_start = math.sqrt(u)

    def RPM(self):
        #dutyCycle = (int(self.entry_y.get()) - 85) * (53 - 49) / (305 - 85) + 49
        #Variable.rpm = math.ceil(dutyCycle / 100 * 4000)
        omega = 2*Variable.velocity_start / (63*0.001) # หาความเร็วเชิงมุม รัศมีของล้อคือ 63 mm
        Variable.rpm = '%.2f' %(omega*60/(2*math.pi)) # แปลงเป็น rpm

    def Moter_voltage(self):
        dutyCycle = (int(self.entry_y.get()) - 85) * (53 - 49) / (305 - 85) + 49 # เทียบค่า dtc กับระยะแกน y
        rpm = math.ceil(dutyCycle / 100 * 4000) # หา rpm จาก dtc
        Variable.voltage = 24 * rpm / 4000 # เทียบบัญญัติไตรยางค์หา voltage
        # V_timport = (int(self.entry_y.get()) - 85) * (2.73 - 2.59) / (305 - 85) + 2.59
        # Variable.voltage = '%.3f' %V_timport
    
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
        self.camvas_frame.update_canvas()

class Button(Frame):    
    def __init__(self, parent):
        super().__init__(parent, bg = '#2B2B2B')
        
        self.next = next_page()
        self.button = ctk.CTkButton(self,
                                    text = 'Next',
                                    width = 25, height = 30,
                                    font = ('Arial', 16),
                                    fg_color = '#99B4DA',
                                    hover_color = "#506988",
                                    text_color = 'black',
                                    corner_radius = 10,
                                    command = self.check_value)
        self.button.pack(side = 'bottom', pady = (0, 10))

    def check_value(self):
        if (Variable.position_x < 150 or Variable.position_x > 390) or (Variable.position_y < 83 or Variable.position_y > 305):
            messagebox.showerror("Error", 'Please enter the correct value of targrt position x and y')
        else:
            next = next_page()
            next()