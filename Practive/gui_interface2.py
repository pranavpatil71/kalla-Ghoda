# this interface is made by ChatGPT
# it is a simple GUI interface for a Python program 
# that allows users to input a Mobile number and name, with display msgbox after submit

import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Kala Ghoda")
root.geometry("400x300")

# Heading Label
heading_label = tk.Label(root, text="***** Kala Ghoda *****", font=("Arial", 16, "bold"))
heading_label.pack(pady=10)

# Username Input
tk.Label(root, text="Enter User Name:").pack()
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Mobile Number Input
tk.Label(root, text="Enter Mobile Number:").pack()
mobile_entry = tk.Entry(root)
mobile_entry.pack(pady=5)

# Button callback function
def on_submit():
    username = username_entry.get()
    mobile = mobile_entry.get()
    
    if not username or not mobile:
        messagebox.showwarning("Input Error", "Please fill both fields.")
        return
    
    # Store or process the data here if needed
    print(f"User Name: {username}")
    print(f"Mobile Number: {mobile}")
    
    # Show a thank you message
    messagebox.showinfo("Success", "Thanks for your Inputs!")
    
    # Simulate next page update
    print("@ This Will be added on another page @@@@@@@")

# Submit Button
submit_button = tk.Button(root, text="Validate & Store", command=on_submit)
submit_button.pack(pady=20)

# Start the GUI loop
root.mainloop()

