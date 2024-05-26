import math
import tkinter as tk
import customtkinter as ctk
from tkinter import Canvas as TkCanvas
from more import Variable, Title, next_page, back_page
from PIL import Image, ImageTk

class Page2(ctk.CTkFrame):
    def __init__(self, parent, size):
        super().__init__(parent, width=size[0], height=size[1], bg_color='#2C2C2C')

        # Define grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # Text
        self.text_frame = Title(self, "Set up your launcher")
        self.text_frame.grid(row=0, column=0, sticky='n', columnspan=3)

        # Canvases
        self.canvas_frame = Canvas(self)
        self.canvas_frame.grid(row=1, column=0, sticky='e')

        # Result
        self.result_frame = Result(self, self.canvas_frame)
        self.result_frame.grid(row=1, column=2, sticky='w')

        # Button
        self.button_frame = Button(self)
        self.button_frame.grid(row=2, column=0, sticky='s', columnspan=3)


class Canvas(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, bg_color='#FFFFFF')
        
        # Create and place canvas for triangle
        self.canvas = TkCanvas(self, width=400, height=364.4, bg='#2C2C2C')
        
        # Draw on canvas
        self.draw_rectangle()
        
        # Layout
        self.canvas.pack()

    def draw_rectangle(self):
        # Declare coordinates for the background
        x0, y0 = 0, 0 # Top left
        x1, y1 = 405, 365 # Bottom right

        # Declare coordinates for the field
        x2, y2 = 30, 30
        x3, y3 = 370, 337

        # Declare coordinates for the launcher
        x4, y4 = 30 + (Variable.position_x * 0.68), 30
        x5, y5 = 30 + 170 + (Variable.position_x * 0.68), 337

        # Draw a filled rectangle (x1, y1, x2, y2)
        self.canvas.create_rectangle(x0, y0, x1, y1, fill="white")
        self.canvas.create_rectangle(x2, y2, x3, y3, fill="#99B4DA", outline="black", width=1)
        self.draw_line()
        self.add_image()

    def add_image(self):
        # Load image
        image = Image.open("Top_view.png")
        image = image.resize((170, 307))
        image = ImageTk.PhotoImage(image)

        # Add image to canvas
        self.canvas.create_image((170 / 2) + (Variable.position_x * 0.68) + 30, 183.5, image=image)
        self.canvas.image = image

    def draw_line(self):
        # Declare coordinates for the line y
        x_coords = [64, 98, 132, 166, 200, 234, 268, 302, 336, 370]
        x_y0, x_y1 = 30, 337

        # Declare coordinates for the line x
        y_coords = [60.7, 91.4, 122.1, 152.8, 183.5, 214.2, 244.9, 275.6, 306.3, 337]
        y_x0, y_x1 = 30, 370

        # Draw line y
        for x in x_coords:
            self.canvas.create_line(x, x_y0, x, x_y1, fill='black', width=1)

        # Draw line x
        for y in y_coords:
            self.canvas.create_line(y_x0, y, y_x1, y, fill='black', width=1)

        if Variable.position_x == 0:
            self.canvas.create_text(202.5 + (Variable.position_x * 0.68), 15, text = "ตั้งเครื่องมุมซ้ายของสนาม", font=('Arial', 16), fill="black", anchor='center')

        if Variable.position_x != 0:
            # Draw range of position launcher change
            self.canvas.create_line(30, 15, 30, 25, fill='black', width=1.5)
            self.canvas.create_line(30 + (Variable.position_x * 0.68), 15, 30 + (Variable.position_x * 0.68), 25, fill='black', width=1.5)
            self.canvas.create_line(30, 20, 30 + (Variable.position_x * 0.68), 20, fill='black', width=1.5)
            self.canvas.create_text(80 + (Variable.position_x * 0.68), 20, text = f"{Variable.position_x} mm.", font=('Arial', 14), fill="black", anchor='center')

    def update_canvas(self):
        self.canvas.delete("all")  # Clear the canvas
        self.draw_rectangle()

class Result(ctk.CTkFrame):
    def __init__(self, parent, canvas_frame):
        super().__init__(parent, width=425, height=300, bg_color='#2B2B2B')

        self.canvas_frame = canvas_frame
        # Create label and text box widgets
        self.label_rpm = ctk.CTkLabel(self, text="RPM : ", font=('Arial', 20))
        self.label_voltage = ctk.CTkLabel(self, text="Motor Voltage : ", font=('Arial', 20))
        
        # Create entry and button widgets
        self.entry_rpm = ctk.CTkEntry(self, placeholder_text='your motor rpm', width=210, height=30, corner_radius=10)
        self.entry_voltage = ctk.CTkEntry(self, placeholder_text='your motor voltage', width=210, height=30, corner_radius=10)

        # Button
        self.Calculate_button = ctk.CTkButton(self, text="Calculate", width=10, height=10, font=('Arial', 12), fg_color='#99B4DA',
                                              hover_color="#506988", text_color='black', command=self.calculate_value)
        
        # Place label, text box, entry, button, and another text widgets using grid layout
        self.label_rpm.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")
        self.entry_rpm.grid(row=1, column=0, padx=20, pady=(5, 15), sticky="w")
        self.label_voltage.grid(row=2, column=0, padx=20, sticky="w")
        self.entry_voltage.grid(row=3, column=0, padx=20, pady=5, sticky="w")
        self.Calculate_button.grid(row=4, column=0, padx=20, pady=(10, 20), sticky="w")

    def calculate_value(self):
        # Declare variable
        Variable.position_x = Variable.position_x - 125
        
        self.text_rpm = ctk.CTkEntry(self, placeholder_text = Variable.rpm, placeholder_text_color='white', width=210, height=30,
                                     corner_radius=10)
        self.text_voltage = ctk.CTkEntry(self, placeholder_text = Variable.voltage, placeholder_text_color='white', width=210, height=30,
                                         corner_radius=10)
        
        # New layout
        self.entry_rpm.grid_forget()
        self.text_rpm.grid(row=1, column=0, padx=20, pady=(5, 15), sticky="w")

        self.entry_voltage.grid_forget()
        self.text_voltage.grid(row=3, column=0, padx=20, pady=5, sticky="w")
        
        # Update canvas
        self.canvas_frame.update_canvas()


class Button(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#2B2B2B')

        next = next_page()
        back = back_page()
        self.button_next = ctk.CTkButton(self, text='Next', width=25, height=30, font=('Arial', 16), fg_color='#99B4DA',
                                        hover_color="#506988", text_color='black', corner_radius=10, command=next)
        self.button_back = ctk.CTkButton(self, text='Back', width=25, height=30, font=('Arial', 16), fg_color='#99B4DA',
                                         hover_color="#506988", text_color='black', corner_radius=10, command=back)
        self.button_next.pack(side='right', padx=(7, 0), pady=(0, 10))
        self.button_back.pack(side='right', padx=(0, 7), pady=(0, 10))
