import subprocess
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

# Function to disconnect a network drive
def disconnect_drive(drive_letter):
    try:
        subprocess.call(f'net use {drive_letter}: /del', shell=True)
        messagebox.showinfo("Success", f"Drive {drive_letter}: disconnected successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to disconnect drive {drive_letter}:\n{e}")

# Function to connect a network drive
def connect_drive(drive_letter, network_path, username, password):
    try:
        subprocess.call(f'net use {drive_letter}: {network_path} /user:{username} {password}', shell=True)
        messagebox.showinfo("Success", f"Drive {drive_letter}: connected to {network_path} successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to connect drive {drive_letter} to {network_path}:\n{e}")

# Function to disconnect all specified drives
def disconnect_all():
    disconnect_drive("D")
    disconnect_drive("L")

# Function to connect all specified drives
def connect_all():
    connect_drive("D", r"\\172.18.1.6\d$", "spdadmin", "spd")
    connect_drive("L", r"\\172.18.0.6\d$", "spdadmin", "spd")

# Create the main window
root = ttk.Window(themename="darkly")
root.title("Network Drive Manager")
root.geometry("600x400")

# Create a frame to hold the buttons and center the frame
frame = ttk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Create and place the "Connect All" button in the frame
btn_connect_all = ttk.Button(frame, text="Connect All Drives", command=connect_all, bootstyle=SUCCESS)
btn_connect_all.pack(pady=10)

# Run the application
root.mainloop()
