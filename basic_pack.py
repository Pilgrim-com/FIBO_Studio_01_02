import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Pack Geometry Manager Example")
root.geometry("300x200")

# Create and pack widgets
label1 = tk.Label(root, text="Label 1", bg="red")
label1.pack(fill=tk.BOTH, expand=True)

label2 = tk.Label(root, text="Label 2", bg="green")
label2.pack(fill=tk.BOTH, expand=True)

label3 = tk.Label(root, text="Label 3", bg="blue")
label3.pack(fill=tk.BOTH, expand=True)

# Start the event loop
root.mainloop()
