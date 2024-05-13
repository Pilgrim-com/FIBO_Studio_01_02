import tkinter as tk
import customtkinter as ctk
from tkinter import *
from more import Variable, Title

class Page2(ctk.CTkFrame):
    def __init__(self, parent, size, next_page, back_page):
        super().__init__(parent, width = size[0], height = size[1], bg_color = '#2B2B2B')
        # Define grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # Text Frame
        self.text_frame = Title(self, 'Result')
        self.text_frame.grid(row = 0, column = 0, sticky='n', columnspan=3)

        # Onput Frame
        self.input_frame = Output(self)
        self.input_frame.grid(row = 1, column = 0, sticky='we', columnspan=3)

        # Button Frame
        self.button_frame = Button(self, next_page, back_page)
        self.button_frame.grid(row = 2, column = 0, sticky='s', columnspan=3)

class Output(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, bg_color = '#2B2B2B')

        #Label
        self.label_x = ctk.CTkLabel(self, text="Launcher Position x :", font = ('Araial', 20))
        self.label_y = ctk.CTkLabel(self, text="Launcher Position y :", font = ('Araial', 20))
        self.label_rpm = ctk.CTkLabel(self, text="RPM :", font = ('Araial', 20))
        self.label_voltage = ctk.CTkLabel(self, text="Moter Voltage :", font = ('Araial', 20))

        #Declare variable
        variable = Variable()

        #Text box by Entry state disabled
        self.text_x1 = ctk.CTkEntry(self, 
                                       placeholder_text = 'x position of launcher (mm)',
                                       font = ('Arial', 16), 
                                       placeholder_text_color = 'white', 
                                       width = 300, height = 45,
                                       corner_radius = 10)
        self.text_y1 = ctk.CTkEntry(self, placeholder_text = 'y position of lanucher (mm)', 
                                       font = ('Arial', 16), 
                                       placeholder_text_color = 'white', 
                                       width = 300, height = 45,
                                       corner_radius = 10)
        self.text_rpm1 = ctk.CTkEntry(self, placeholder_text = 'rpm',
                                       font = ('Arial', 16), 
                                       placeholder_text_color = 'white', 
                                       width = 300, height = 45,
                                       corner_radius = 10)
        self.text_voltage1 = ctk.CTkEntry(self, placeholder_text = 'voltage', 
                                       font = ('Arial', 16), 
                                       placeholder_text_color = 'white', 
                                       width = 300, height = 45,
                                       corner_radius = 10)

        # Create button for Calculate
        self.button_cal = ctk.CTkButton(self,
                                        text="Calculate",
                                        width = 10, height = 10,
                                        font = ('Arial', 12),
                                        fg_color = '#99B4DA',
                                        hover_color = "#506988",
                                        text_color = 'black',
                                        command = self.calculate_value)

        # Define grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        #Layout
        self.label_x.grid(row = 0, column = 0, sticky = 'w', padx = 100, pady = (20, 0))
        self.label_rpm.grid(row = 0, column = 1, sticky = 'w', padx = 100, pady = (20, 0))
        self.text_x1.grid(row = 1, column = 0, sticky = 'w', padx = 100, pady = 5)
        self.text_rpm1.grid(row = 1, column = 1, sticky = 'w', padx = 100, pady = 5)
        self.label_y.grid(row = 2, column = 0, sticky = 'w', padx = 100)
        self.label_voltage.grid(row = 2, column = 1, sticky = 'w', padx = 100)
        self.text_y1.grid(row = 3, column = 0, sticky = 'w', padx = 100, pady = 5)
        self.text_voltage1.grid(row = 3, column = 1, sticky = 'w', padx = 100, pady = 5)
        self.button_cal.grid(row = 4, column = 0, columnspan = 2, sticky = 's', pady = 10 )
    
    def calculate_value(self):
        #Declare variable
        variable = Variable()

        #Text box by Entry state disabled
        self.text_x = ctk.CTkEntry(self, 
                                       placeholder_text = str(variable.position_x),
                                       font = ('Arial', 18), 
                                       placeholder_text_color = 'white', 
                                       width = 300, height = 45,
                                       corner_radius = 10)
        self.text_y = ctk.CTkEntry(self, placeholder_text = str(variable.position_y), 
                                       font = ('Arial', 18), 
                                       placeholder_text_color = 'white', 
                                       width = 300, height = 45,
                                       corner_radius = 10)
        self.text_rpm = ctk.CTkEntry(self, placeholder_text = str(variable.rpm),
                                       font = ('Arial', 18), 
                                       placeholder_text_color = 'white', 
                                       width = 300, height = 45,
                                       corner_radius = 10)
        self.text_voltage = ctk.CTkEntry(self, placeholder_text = str(variable.voltage), 
                                       font = ('Arial', 18), 
                                       placeholder_text_color = 'white', 
                                       width = 300, height = 45,
                                       corner_radius = 10)
        
        print(variable.position_x)
        print(variable.position_y)
        print(variable.rpm)
        print(variable.voltage)
        
        # New layout
        self.text_x1.grid_forget()
        self.text_x.grid(row = 1, column = 0, sticky = 'w', padx = 100, pady = 5)

        self.text_rpm1.grid_forget()
        self.text_rpm.grid(row = 1, column = 1, sticky = 'w', padx = 100, pady = 5)

        self.text_y1.grid_forget()
        self.text_y.grid(row = 3, column = 0, sticky = 'w', padx = 100, pady = 5)

        self.text_voltage1.grid_forget()
        self.text_voltage.grid(row = 3, column = 1, sticky = 'w', padx = 100, pady = 5)

class Button(ctk.CTkFrame):
    def __init__(self, parent, next_page, back_page):
        super().__init__(parent, bg_color = '#2B2B2B')

        self.button_sim = ctk.CTkButton(self,
                                    text = 'Next',
                                    width = 25, height = 30,
                                    font = ('Arial', 16),
                                    fg_color = '#99B4DA',
                                    hover_color = "#506988",
                                    text_color = 'black',
                                    corner_radius = 10,
                                    command = next_page)
        self.button_back = ctk.CTkButton(self,
                                    text = 'Back',
                                    width = 25, height = 30,
                                    font = ('Arial', 16),
                                    fg_color = '#99B4DA',
                                    hover_color = "#506988",
                                    text_color = 'black',
                                    corner_radius = 10,
                                    command = back_page)
        self.button_sim.pack(side='right', padx=(7, 0), pady=(0, 10))
        self.button_back.pack(side='right', padx=(0, 7), pady=(0, 10))