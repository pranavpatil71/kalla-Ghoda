import tkinter as tk
import gui_fuel_fulltankmethod_def as ftm1
import gui_fuel_reservetankmethod_def as rtm1

class fuelmeterclass:
    def __init__ (self,fuelframe):
        self.tankmethod=tk.StringVar()
        tk.Radiobutton(fuelframe,text='Full tank method',variable=self.tankmethod,value="fullTankMethod").pack(pady=5)
        tk.Radiobutton(fuelframe,text='reserve indicator method', variable=self.tankmethod,value="reserveTankMethod").pack(pady=5)
        #tk.Radiobutton(fuelframe, text="reservetank", variable=self.tankmethod, value="ReserveTankMethodVariable").pack(pady=5)
        tk.Button(fuelframe,text="submit",command=self.submit).pack(pady=5)

    def submit(self):
        value=self.tankmethod.get()
        print("Hi There, You are Into Milage Calculation method", value.lower())
        if value=='fullTankMethod':
            milage=ftm1.fulltankmethod()
            print("Milage is - ",milage)
            tk.mainloop()
        elif value=='reserveTankMethod':
            rtm1.reserve_tank()
            tk.mainloop()
        
          

def fuelmeter():
    fuelframe=tk.Toplevel(bg="lightblue", width=200, height=100)
    fuelframe.title("Fuel Meter")
    fuelframe.geometry("500x250")
    tk.Label(fuelframe,text="Check Your Bikes Milage Based on Below Parameter").pack(pady=5)
    tk.Label(fuelframe,text="Select only one method at a time").pack(pady=5)
    c1=fuelmeterclass(fuelframe)

