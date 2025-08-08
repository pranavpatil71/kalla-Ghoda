import tkinter as tk
from tkinter import messagebox
import sqlite3 as qlit

def userdata():
    def submit():
        uname=UserNameEntry.get()
        umobile=UserMobileNoEntry.get()
        ubike=UserBikeNameEntry.get()
        connection=qlit.connect('AddMaintanace_db.db')
        cursor=connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS userdata (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                usercontact TEXT NOT NULL,
                userbike TEXT NOT NULL
            )            
        ''')

        cursor.execute('INSERT INTO userdata (username,usercontact,userbike) values(?,?,?)',(uname,umobile,ubike))
        connection.commit()
        connection.close()
        print("Data added successfully")
        messagebox.showinfo("Greetings", "Congrats, Your Data Saved Successfully !!!")

    frame1 = tk.Tk()
    frame1.title("Kallaa Ghoda")
    frame1.geometry("450x150")

    UserNameLabel=tk.Label(frame1,text="User Name :").pack()
    UserNameEntry=tk.Entry(frame1)
    UserNameEntry.pack()

    UserMobileNoLabel=tk.Label(frame1,text="Mobile No :").pack()
    UserMobileNoEntry=tk.Entry(frame1)
    UserMobileNoEntry.pack()

    UserBikeNameLabel=tk.Label(frame1,text="Bike Name :").pack()
    UserBikeNameEntry=tk.Entry(frame1)
    UserBikeNameEntry.pack()

    submitButton= tk.Button(frame1, text="Submit", command=submit).pack(pady=5)
    tk.mainloop()


'''def main():
    userdata()

if __name__==("__main__"):
    main()
'''
