import tkinter as tk
import sqlite3 as qlit

def visualize_data():
    conn = qlit.connect('AddMaintanace_db.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM user_maintenance;
    ''')
    #SELECT ProblemDetails FROM user_maintenance WHERE SparePart='b'; 
    data=cursor.fetchall()
    display(data)
    #print(data)
    conn.commit()
    conn.close()

def display(data):
    displayframe=tk.Tk()
    displayframe.title("OutPut of data")
    displayframe.geometry("300x150")
    for i in data:
        tk.Label(displayframe,text=i).pack(pady=5)
    tk.mainloop()