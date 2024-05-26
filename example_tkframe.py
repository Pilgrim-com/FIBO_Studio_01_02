import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Basic Frame Example")
root.geometry("300x200")

# Create a frame within the main window
frame = tk.Frame(root, bg="lightblue", width=200, height=100)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Add a label to the frame
label = tk.Label(frame, text="Hello, Tkinter!", bg="lightblue")
label.pack(pady=10)

# Add a button to the frame
button = tk.Button(frame, text="Click Me!")
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
