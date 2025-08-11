# This window will calculate total maintaince of Bike
# frm stands for frame and mntc is maintainace, so frm mntc is maintance record adding frame
# & lbl is label
# & ntry is entry

def maintenace():
    
    from tkinter import messagebox
    import tkinter as tk
    import sqlite3 as glit

    def submit_maintainance():
            messagebox.showinfo("Success","Details Added successfully")
            FrameMaintainance.destroy()# remove this incase of multiple data entry

    def db_connect():
        #This function create database with respect to your coloums
        problemdetails=Ntry_ProblemDetails.get()
        part_name=Ntry_SparePart.get()
        part_cost=Ntry_PartCost.get()
        laborcost=Ntry_LaborCost.get()
        addon=Ntry_AdditionalCost.get()
        desc=Ntry_Descriptions.get()

        conn = glit.connect('AddMaintanace_db.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_maintenance  (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ProblemDetails TEXT NOT NULL,
                    SparePart TEXT NOT NULL,
                    SpareCost TEXT NOT NULL,
                    LaborCost TEXT NOT NULL,
                    AdditionalCost TEXT NOT NULL,
                    Descriptions TEXT NOT NULL                    
                )
        ''')

        #cursor.execute('INSERT INTO user_maintenance (SparePart) VALUES (?)',('C'))
        cursor.execute('INSERT INTO user_maintenance (ProblemDetails,SparePart,SpareCost,LaborCost,AdditionalCost,Descriptions) VALUES (?,?,?,?,?,?)', (problemdetails,part_name,part_cost,laborcost,addon,desc))
        conn.commit()
        print("Data Entered Successfully")
        submit_maintainance()
        conn.close()


    FrameMaintainance =tk.Tk()
    FrameMaintainance.title("Add Maintance Details")
    FrameMaintainance.geometry("250x400")

    Lbl_ProblemDetails= tk.Label(FrameMaintainance, text="Problem Details").pack()
    Ntry_ProblemDetails = tk.Entry(FrameMaintainance)
    Ntry_ProblemDetails.pack() # since pack widgets seperately

    Lbl_SparePart= tk.Label(FrameMaintainance, text="Changed Spare Part Name").pack()
    Ntry_SparePart = tk.Entry(FrameMaintainance)
    Ntry_SparePart.pack() 

    Lbl_PartCost= tk.Label(FrameMaintainance, text="Spare part cost").pack()
    Ntry_PartCost = tk.Entry(FrameMaintainance)
    Ntry_PartCost.pack() 

    Lbl_LaborCost= tk.Label(FrameMaintainance, text="Labor cost").pack()
    Ntry_LaborCost = tk.Entry(FrameMaintainance)
    Ntry_LaborCost.pack() 

    Lbl_AdditionalCost= tk.Label(FrameMaintainance, text="Additional cost if any").pack()
    Ntry_AdditionalCost = tk.Entry(FrameMaintainance)
    Ntry_AdditionalCost.pack() 

    Lbl_Descriptions= tk.Label(FrameMaintainance, text="Descriptions").pack()
    Ntry_Descriptions = tk.Entry(FrameMaintainance)
    Ntry_Descriptions.pack() 

    btn_submit = tk.Button(FrameMaintainance, text="Submit", command= db_connect).pack(pady=5)

    tk.mainloop()

def main():
     maintenace()

if __name__ == "__main__" :
    main()