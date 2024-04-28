import tkinter as tk
from tkinter import *
from Page1 import Page1
from Page2 import Page2
from Page3 import Page3

class Main_App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])

        self.current_page = 0
        page1 = Page1(self, size, self.next_page)
        page2 = Page2(self, size, self.next_page, self.back_page, page1)
        page3 = Page3(self, size, self.back_page)
        self.pages = [page1, page2, page3]

        self.pages[self.current_page].pack(fill=tk.BOTH, expand=True)

    def next_page(self):
        self.pages[self.current_page].pack_forget()  # Hide current page
        self.current_page = (self.current_page + 1) % len(self.pages)  # Move to next page
        self.pages[self.current_page].pack(fill=tk.BOTH, expand=True)  # Show next page

    def back_page(self):
        self.pages[self.current_page].pack_forget()  # Hide current page
        self.current_page = (self.current_page - 1) % len(self.pages)  # Move to previous page
        self.pages[self.current_page].pack(fill=tk.BOTH, expand=True)  # Show previous page

# Create and run the app
app = Main_App('Simulation', (850, 600))
app.mainloop()