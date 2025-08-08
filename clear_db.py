import sqlite3 as qlit
connection=qlit.connect('AddMaintanace_db.db')
cursor=connection.cursor()

print("User maintaince table contains below items")
cursor.execute('select * from user_maintenance')
data=cursor.fetchall()
print(data)

response=input("If you want to delete complete table enter 1 else change id in code: ")
if response=='1':
    cursor.execute('drop table user_maintenance')
    print("complete table is deleted")
else:
    #Add Id that u wants to delete.
    cursor.execute("delete from user_maintenance where id='2';")
    print("selected Id is deleted")

connection.commit()
connection.close()