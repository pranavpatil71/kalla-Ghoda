import tkinter as tk


class fuelmeterclass:
    def method1(self):
        res = self.radiobuttonmethod.get()
        print("Into Method", res)

    def __init__(self, fuelMeterFrame):

        self.radiobuttonmethod=tk.StringVar()
        FullTankrb1=tk.Radiobutton(fuelMeterFrame,text='Full tank method',variable=self.radiobuttonmethod,value="fulTankMethodx").pack()
        ReserveTabkrb1=tk.Radiobutton(fuelMeterFrame,text='reserve indicator method', variable=self.radiobuttonmethod,value="reserveTankMethod").pack()
        #res=self.radiobuttonmethod.get()
        tk.Button(fuelMeterFrame, text="Submit", command=self.method1).pack(pady=5)



def fuelmeter():
    fuelMeterFrame=tk.Tk()
    fuelMeterFrame.title("Fuel Inputs")
    fuelMeterFrame.geometry('500x500')
    tk.Label(fuelMeterFrame,text="Check Your Bikes Milage Based on Below Parameter").pack()
    tk.Label(fuelMeterFrame,text="Select only one method at a time").pack()
    c1=fuelmeterclass(fuelMeterFrame)
    tk.mainloop()






