import tkinter as tk
import customtkinter as ctk
from tkinter import *
from Simulayion_page import Page3
from Result_page import Page2
from Input_page import Page1

class Main_App(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        
        # Config theme and color
        ctk.set_default_color_theme('blue')  # Themes: "blue" (standard), "green", "dark-blue"
        ctk.set_appearance_mode("dark") # Modes: 'light' (standart), 'dark'

        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])

        #declare variable
        self.current_page = 0
        
        page1 = Page1(self, size, self.next_page)
        page2 = Page2(self, size, self.next_page, self.back_page)
        page3 = Page3(self, size, self.back_page)
        self.pages = [page1, page2, page3]

        self.pages[self.current_page].pack(fill = 'both', expand = True)

    def next_page(self):
        self.pages[self.current_page].pack_forget()  # Hide current page
        self.current_page = (self.current_page + 1) % len(self.pages)  # Move to next page
        self.pages[self.current_page].pack(fill = 'both', expand = True)  # Show next page

    def back_page(self):
        self.pages[self.current_page].pack_forget()  # Hide current page
        self.current_page = (self.current_page - 1) % len(self.pages)  # Move to previous page
        self.pages[self.current_page].pack(fill = 'both', expand = True)  # Show previous page

# Create and run the app
app = Main_App('Simulation', (850, 600))
app.mainloop()