#main.py
# Add an import statement for Vehicle class

from vehiclePackage.vehicleClass import *

if __name__ == "__main__":
    #instantiate an object if type vehicle
    myCorvette = Vehicle("Car", 120) #Trigger a call to constructor
    myCorvette.printType()      #Invoke the method on the object
    
    # Invoke the getter for maximum speed, store the return value to the variable
    # print that to the console.
    
    maximum_speed = myCorvette.getSpeed()
    print("Maximum speed:", maximum_speed)
    
    # instantiate another Vehicle object. You can name it. 
    myCorolla = Vehicle("Car", 80)  #myCorolla us an object of type Vehicle
    
    
    # I want a list of 3 Vehicles: Car, Boat, Space Ship
    # You can pick the names and properties
    # I want some friendly output to demo your work
    
    myVehicles = [ Vehicle("Dodge Hellcat", 150)
                  ,Vehicle("Yacht", 100)
                  ,Vehicle("Falcon Heavy", 4000)]
# iterate over the list
for vehicle in myVehicles:
    vehicle.printType()
    print (vehicle.getSpeed())    