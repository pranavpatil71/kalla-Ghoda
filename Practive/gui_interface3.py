# This is test interface made by me
#0
import tkinter as tk

# Simple Interface which will take entry of user.

#1.
root = tk.Tk()

root.title("Kaala Ghoda")
root.geometry("400x150")

#2
userNameLabel = tk.Label(root,text="Enter User Name")
userNameLabel.pack()
entryNameLabel = tk.Entry(root)
entryNameLabel.pack(pady=5)

tk.Label(root, text="Enter Mobile Number:").pack()
tk.Entry(root).pack(pady=5)

#3
tk.mainloop()