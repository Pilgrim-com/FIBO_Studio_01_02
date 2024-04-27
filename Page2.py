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

        # Text Frame
        self.text_frame = Title(self)
        self.text_frame.grid(row = 0, column = 0, sticky='n', columnspan=3)

        # Onput Frame
        self.input_frame = Output(self)
        self.input_frame.grid(row = 1, column = 0, sticky='we', columnspan=3)

        # Button Frame
        self.back_frame = Button(self)
        self.back_frame.grid(row = 2, column = 0, sticky='w', columnspan=3)

class Title(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="Result", font="Inter 32 bold")
        self.label.pack()
        #self.label.place(relx=0.5, rely=0.03, anchor='center')

class Output(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)

        #Label
        self.label_x = tk.Label(self, text="Position x (mm)", font="Inter 16")
        self.label_y = tk.Label(self, text="Position y (mm)", font="Inter 16")
        self.label_rpm = tk.Label(self, text="RPM", font="Inter 16")
        self.label_voltage = tk.Label(self, text="Moter Voltage", font="Inter 16")

        #Text box
        self.text_x = tk.Text(self, width = 20, height = 2)
        self.text_y = tk.Text(self, width = 20, height = 2)
        self.text_rpm = tk.Text(self, width = 20, height = 2)
        self.text_voltage = tk.Text(self, width = 20, height = 2)

        #Insert text to text box
        self.text_x.insert('1.0', "Position x")
        self.text_y.insert('1.0', "Position y")
        self.text_rpm.insert('1.0', "1242 rpm")
        self.text_voltage.insert('1.0', "2.71 V")

        #State edit
        self.text_x.config(state = 'disabled')
        self.text_y.config(state = 'disabled')

        #Layout
        self.label_x.grid(row = 0, column = 0, sticky = 'w', padx = 10)
        self.label_rpm.grid(row = 0, column = 2, sticky = 'w', padx = 10)
        self.text_x.grid(row = 1, column = 0, sticky = 'w', padx = 10, pady = 5)
        self.text_rpm.grid(row = 1, column = 2, sticky = 'w', padx = 10, pady = 5)
        self.label_y.grid(row = 2, column = 0, sticky = 'w', padx = 10)
        self.label_voltage.grid(row = 2, column = 2, sticky = 'w', padx = 10)
        self.text_y.grid(row = 3, column = 0, sticky = 'w', padx = 10, pady = 5)
        self.text_voltage.grid(row = 3, column = 2, sticky = 'w', padx = 10, pady = 5)

class Button(tk.Frame):
    def Back():
        back = 1
    def __init__(self, parent):
        super().__init__(parent)

        self.button_sim = tk.Button(self, text='Simulation', command=self.Back)
        self.button_back = tk.Button(self, text='Back', command=self.Back)
        self.button_sim.pack(side='right', padx=5, pady=5)
        self.button_back.pack(side='right', padx=5, pady=5)

# Create and run the app
app = App('Simulation', (850, 600))