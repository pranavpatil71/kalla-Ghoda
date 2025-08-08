import tkinter as tk
import gui_Maintainance as m10
import gui_userdetails5 as ud1
import gui_visualise_maintainanceData as mv1
import gui_fuelmeter3 as fm3

FrameHome = tk.Tk()
FrameHome.title("HomeScreen")
FrameHome.geometry("1000x450")

Btn_UserDetails = tk.Button(FrameHome,text="Add Your Details",command=ud1.userdata).pack(pady=5)
Btn_UserMaintenance = tk.Button(FrameHome,text="Add Your Maintenance",command=m10.maintenace).pack(pady=5)
btn_fuelConsumption = tk.Button(FrameHome,text="Add Fuel Consumption", command=fm3.fuelmeter).pack(pady=5)
btn_ShowExpenditure = tk.Button(FrameHome,text="Your Maintenance Investment",command=mv1.visualize_data).pack(pady=5)

tk.mainloop()
