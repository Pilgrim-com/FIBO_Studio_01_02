import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Place Geometry Manager Example")
root.geometry("300x200")

# Create and place widgets
label1 = tk.Label(root, text="Label 1", bg="red")
label1.place(x=50, y=50, width=100, height=50)

label2 = tk.Label(root, text="Label 2", bg="green")
label2.place(x=160, y=50, width=100, height=50)

label3 = tk.Label(root, text="Label 3", bg="blue")
label3.place(x=105, y=110, width=100, height=50)

# Start the event loop
root.mainloop()
