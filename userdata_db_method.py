#userdata db method
import tkinter as tk
import sqlite3 as qlt


def userdatadb():
    conn= qlt.Connection('AddMaintanace_db.db')
    cursor=conn.cursor()
    cursor.execute('select * from userdata')
    info=cursor.fetchall()
    for i in info:
        print(i)
    conn.commit()
    conn.close()

userdatadb()