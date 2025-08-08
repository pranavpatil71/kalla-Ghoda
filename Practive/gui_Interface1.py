# this interface is made by CoPilot
# it is a simple GUI interface for a Python program 
# that allows users to input a Mobile number and name, with display msgbox after submit 
import tkinter as tk
from tkinter import messagebox

def greetings():
    messagebox.showinfo("Greetings", "Thanks for your Inputs")

def submit():
    username = entry_username.get()
    mobile_no = entry_mobile.get()
    if username and mobile_no:
        greetings()
    else:
        messagebox.showwarning("Input Error", "Please enter both User Name and Mobile Number.")

def pageupdate():
    messagebox.showinfo("Page Update", "@ This Will be added on another page @@@@@@@")

root = tk.Tk()
root.title("Kala Ghoda App")

# Heading
heading_label = tk.Label(root, text="*****Kala Ghoda*****", font=("Arial", 16))
heading_label.pack(pady=10)

# Username
label_username = tk.Label(root, text="Enter User Name")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

# Mobile Number
label_mobile = tk.Label(root, text="Enter Mobile Number")
label_mobile.pack()
entry_mobile = tk.Entry(root)
entry_mobile.pack()

# Submit Button
submit_button = tk.Button(root, text="Validate and Store Response", command=submit)
submit_button.pack(pady=10)

# Page Update Button (optional)
pageupdate_button = tk.Button(root, text="Page Update", command=pageupdate)
pageupdate_button.pack(pady=5)

root.mainloop()