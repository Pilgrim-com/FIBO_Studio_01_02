import customtkinter as ctk
from tkinter import *

class Variable:
    position_x = 0
    position_y = 0
    velocity_start = 0
    rpm = 0
    voltage = 0
    
    """ def __init__(self):
        self.position_x = 0
        self.position_y = 0
        self.velocity_start = 0
        self.rpm = 0
        self.voltage = 0

    def update_position_x(self, new_value):
        self.position_x = new_value

    def update_position_y(self, new_value):
        self.position_y = new_value

    def update_velocity_start(self, new_value):
        self.velocity_start = new_value

    def update_rpm(self, new_value):
        self.rpm = new_value

    def update_voltage(self, new_value):
        self.voltage = new_value """

class Title(ctk.CTkFrame):
    def __init__(self, parent, title):
        super().__init__(parent, bg_color = '#2C2C2C')
        self.label = ctk.CTkLabel(self, text = title, font = ('Inter', 32))
        self.label.pack()
        