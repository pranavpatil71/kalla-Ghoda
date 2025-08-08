import tkinter as tk

'''
#this file contains method to calculate fuel consumption
print("Consider Fuel Rate at 105Rs per liter and Input following Data")
petrolRate=105
fuel=float(input("Enter Fuel in liter : "))
totalcost=petrolRate*fuel
print("TotalCost = ", totalcost)

#Range Calculation
speedometer_reading=int(input("Enter your speedometer reading : "))
milage=40
range=milage*fuel
print("Your Range of this trip expected to be ",range,'kms',"\nYour should fill next petrol before ", speedometer_reading+range,"kms")
'''

#average calculation
#1. empty tank ,speedometer reading, full tank, empty tank, last speedometer reading 
#-  0liter     ,100               , 11 litre ,-11 liter  , 210 milage = 210-100km/11liter= 10km/ltr

#2. non emptr tank, speedometer reading, full tank, drive, refill empty tank, last speedometer reading
#-  xliter        , 100                , 4 liter  ,      , 4 liter          , 140   milage= 140-100km/4refilliter=10 km/ltr

#3. empty tank, 1 liter perol, odo reading, petrol end odo
#-  0liter    , 1 liter.     , 100        , 110 milage = 110-100/1 liter= 10km\litr

#4. researve tank cap = 2.5 liter, non empty, fill fuel, total in bike, odo reading and turn fuel to 'on', fuel on to reaserve odo, next fill fuel, odo now, fuel ends to reserve odo, 
#                                   xliter  , 3 liter  , x+3          , 100                              , 120,                   , 3 liter       , 130.   , 240,                     
# first milage on reserve tank pre cap = 120 - 100/ 3 - 2.5 = 20/0.5 = 40 km/liter
# second milege based on later comp = 240-120/ 3nxt liter = 40 km/ liter
# calculate based on way 4 for 4 times and get avg of your milage.
def method(x):
    print("Into Method", x.lower())
    x=fuelmeter.radiobuttonmethod.get()
    print("Into Method", x.lower())

def fuelmeter():
    fuelMeterFrame=tk.Tk()
    fuelMeterFrame.title("Fuel Inputs")
    fuelMeterFrame.geometry('500x500')
    radiobuttonmethod=tk.StringVar(value="")
    '''
    def fulTankMethod():
        print("Into fulTankMethod")

    def reserveTankMethod():
        print("Into reserveTankMethod")
    
    def radiobuttonmethod():
        print("Into radiobuttonmethod")
   
    
    def method(x):
        print("Into Method", x.lower())
     '''
    
    #radiobuttonmethod=tk.StringVar(value='')
    tk.Label(fuelMeterFrame,text="Check Your Bikes Milage Based on Below Parameter").pack()
    tk.Label(fuelMeterFrame,text="Select only one method at a time").pack()

    FullTankrb1=tk.Radiobutton(fuelMeterFrame,text='Full tank method',variable=radiobuttonmethod,value="fulTankMethodx").pack()
    ReserveTabkrb1=tk.Radiobutton(fuelMeterFrame,text='reserve indicator method', variable=radiobuttonmethod,value="reserveTankMethod").pack()

    #tk.Button(fuelMeterFrame,text='submit your response', command=method).pack(pady=5)
    tk.Button(fuelMeterFrame, text="Submit", 
            command=lambda: method(radiobuttonmethod.get()) if radiobuttonmethod.get() else print("Error", "No gender selected")).pack(pady=20)

    tk.mainloop()


