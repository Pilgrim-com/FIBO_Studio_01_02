import tkinter as tk
import customtkinter as ctk

# Initialize the main window
root = tk.Tk()
root.title("Basic CTkFrame Example")
root.geometry("300x200")

# Set the appearance mode of the customtkinter
ctk.set_appearance_mode("dark")  # Options: "dark", "light", "system"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

# Create a CTkFrame within the main window
frame = ctk.CTkFrame(root, corner_radius=10)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.8, relheight=0.5)

# Add a label to the CTkFrame
label = ctk.CTkLabel(master=frame, text="Hello, CustomTkinter!", fg_color=None)
label.pack(pady=10)

# Add a button to the CTkFrame
button = ctk.CTkButton(master=frame, text="Click Me!")
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
