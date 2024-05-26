import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Grid Weight Example")
root.geometry("300x200")

# Create and grid widgets
label1 = tk.Label(root, text="Label 1", bg="red")
label1.grid(row=0, column=0, sticky="nsew")

label2 = tk.Label(root, text="Label 2", bg="green")
label2.grid(row=0, column=1, sticky="nsew")

label3 = tk.Label(root, text="Label 3", bg="blue")
label3.grid(row=1, column=0, columnspan=2, sticky="nsew")

# Configure grid rows and columns with weight
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=2)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)

# Start the event loop
root.mainloop()

