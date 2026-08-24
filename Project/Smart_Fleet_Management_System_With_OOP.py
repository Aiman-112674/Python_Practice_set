# Project:: Smart Fleet Management System using Objected Oriented Programming in Python 

#start
class Vehicle:
    def __init__(self,brand,model,vin):
        self.brand = brand 
        self.model = model 
        self.__vin = vin 
    def get_vin(self):
        return self.__vin
    def get_info(self):
        return(f"My Vehicle Brand is  {self.brand} ,the model is {self.model} ")

class GasEngine:
    def refuel(self):
        print("Tank Filled with Gasoline")

class ElectricMotor:
    def recharge(self):
        print("Battery Charged via plug")

class HybirdVehicle(Vehicle,GasEngine,ElectricMotor):
    def __init__(self,brand , model , vin , battery_capacity ):
        super().__init__(brand,model,vin)
        self.battery_capacity= battery_capacity
    def drive_hybird(self):
        print(f"The Hybird Vehicle is driving .!")
class FleetGarage:
    def __init__(self):
        self.vehicles = []
    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)

    def __iter__(self):
        self._index = 0
        return self
    def __next__(self):
        if self._index < len(self.vehicles):
            vehicle = self.vehicles[self._index]
            self._index +=1
            return vehicle
        else:
            raise StopIteration
def service_remainder(vehicle_list,mileage_threshold):
    for vehicle , mileage in vehicle_list:
        if mileage>mileage_threshold:
            yield f"Service Alert : {vehicle.brand} {vehicle. model} needs service! Mileage: {mileage} miles "



v1 = Vehicle("Toyota" , "Corolla" , "VIN98765")
v2 = HybirdVehicle("Toyota" , "Prius" , "VIN 12345" ,battery_capacity=8.8)
v3 = HybirdVehicle("Honda" , "Accord Hybird" , "VIN54321" , battery_capacity=1.3)

print("----Vehicle Features Test ----")
v2.refuel()
v2.recharge()
v2.drive_hybird()
print("Accessing private VIN via getter:" , v2.get_vin())
print()

print("---Fleet Inventory (Custom Iterator Loop) ---")
garage = FleetGarage()
garage.add_vehicle(v1)
garage.add_vehicle(v2)
garage.add_vehicle(v3)

for car in garage:
    print("Found in Garage: " , car.get_info())
print()

print("---Generator Function (Maintenance Alerts) ---")
fleet_mileage = [(v1,45000) , (v2,78000) , (v3,12000)]

alert_generator = service_remainder(fleet_mileage,mileage_threshold=50000)
for alert in alert_generator:
    print(alert)
print()


print("----Generator Expression (Speed Check)----")
logged_speeds = [42,68,55,88,71]
speed_warnings = (
    f"ALERT: Vehicle logged at {spd} mph! (Exceeds 60 mph)"
    for spd in logged_speeds
    if spd > 60
)

for waring in speed_warnings:
    print(waring)
