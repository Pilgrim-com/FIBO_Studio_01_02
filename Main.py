import customtkinter as ctk
from Simulayion_page import Page3
from Setup_page import Page2
from Input_page import Page1
from more import Variable

class Main_App(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        
        # Config theme and color
        ctk.set_default_color_theme('blue')  # Themes: "blue" (standard), "green", "dark-blue"
        ctk.set_appearance_mode("dark") # Modes: 'light' (standart), 'dark'

        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.resizable(False, False)
        
        page1 = Page1(self, size)
        page2 = Page2(self, size)
        page3 = Page3(self, size)
        Variable.pages = [page1, page2, page3]

        Variable.pages[Variable.current_page].pack(fill = 'both', expand = True)

# Create and run the app
app = Main_App('Simulation', (850, 600))
app.mainloop()