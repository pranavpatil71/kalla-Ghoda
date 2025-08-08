# Self Made GUI Interface for my app with Entry box and submit button with acknowlegment button functionality.

#1.
import tkinter as tk
from tkinter import messagebox

#6
def submit():
    UserName=LabelEntry.get()
    messagebox.showinfo("Greetings"," Entered Successfully")
    
#2.
root=tk.Tk()

root.title("kallaa Ghoda")
root.geometry("400x150")

#3.
LabelName= tk.Label(root, text="Enter User Name").pack()

#4
LabelEntry= tk.Entry(root)
LabelEntry.pack() #Rule - Widget should Aways Pack it seperately, not in one line

#5
button1 = tk.Button(root,text="Submit",command=submit).pack()

#7
tk.mainloop()
