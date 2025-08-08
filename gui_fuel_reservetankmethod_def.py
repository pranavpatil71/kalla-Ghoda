#reserve tank meter
# reaserve tank size = 2.5 liter

def reserve_tank():
    print("Lets assume reserve tank size of 2.5 liter : ")
    response=input("is your Bike into a reaserve mode Add Yes or No : ")
    if response==('Yes' or 'yes' or 'y' or 'Y'):
        print("response as Yes, Please add more than 2.5 liters petrol for best result")
        read1=int(input("Enter reading odo : "))
        fu1=int(input("Enter fuel ur adding : "))
        read2=int(input("Enter odo when bike got again into researve : "))
        milage = (read2-read1)/fu1
        print("Milage", milage)

    elif response==('No' or 'no' or 'n' or 'N'):
        print("response as No")
        print("Please any liters of petrol as more than 2.5 already exist into your tank")
        ful1=int(input("Enter fuel ur adding : "))
        read3=int(input("Enter odo reading while first fueling : "))
        print("Please ride vehicle carefully and put a petrol again on reasearve once u back to fuel station")
        read4=int(input("Enter odo when bike got into researve : "))
        ful2= int(input("Enter Fuel you are adding "))
        read5=int(input("Enter odo when bike got into researve again: "))

        milage = (read5-read4)/ful2
        print("Milage", milage)

    itr=input("For More safer side, lets try multiple iteration, to continue Yes stop No")
    if(itr=='Yes'):
    #find milage0 with this data 

        print("You will be adding fuel once your know fuel Indicator or bike got researve")
        odo1=int(input("Enter ODO Meter Reading Before fueling : "))
        fuel1=int(input("Enter Fuel in liters you have added : "))
        odo2=int(input("Enter ODO reading once bike goes reserve nd u filled petrol : "))
        odo3=int(input("Optional reading when u add petrol in case later : "))
        fuel2=int(input("Enter quantity of fuel you have added : "))
        odo4=int(input("Enter ODO reading once bike goes reaserve again : "))

        total_fuel_consumed=fuel1+fuel2
        avg2=(odo4-odo3)/fuel2
        avg1=(odo2-odo1)/fuel1
        avg3=(avg2+avg1)/2

        print("milage1 ",avg1 )
        print("milage2 ",avg2)
        print("avgerage milage of bike ",avg3)

#reserve_tank()