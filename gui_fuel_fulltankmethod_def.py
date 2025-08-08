#gui fuel meter def


def fulltankmethod():
    reading = input("Enter fuel tank reading: (Empty/Not So Full/Reserve) : ")
    # expected liter remaining
    filledpetrol = float(input("Amount of petrol filled to completely fill your tank: "))
    #totalfuelinbike = reading + filledpetrol

    odoread = float(input("Reading of odoo while first fuelling: "))
    print("Please ride vehicle carefully and put a petrol again once u back to fuel station")
    odo2read = float(input("Enter odoo reading when fuel consumed, while second refuelling: "))
    filledpetrol2= float(input("Amount of petrol filled to completely fill your tank: "))

    # odo difference gives you reading 
    # divide it by petrol filled to get mileage 
    ododiff = odo2read - odoread
    milage = ododiff / filledpetrol2

    return milage


