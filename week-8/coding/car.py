class Car(object):
    def __init__(self, color,model,year,engine_on=False,fuel_level=100):
        self.color = color
        self.model=model
        self.year=year
        self.fuel_level=fuel_level
        self.engine_on=engine_on
    def start_engine(self):
        if self.fuel_level == 0:
            print("No fuel! Cannot start engine")
            return
        if self.engine_on:
            print("Engine is already on")
            return
        self.engine_on=True
        print("The car engine has started")
    def stop_engine(self):
        if not self.engine_on:
            print("Engine is already off!")
            return
        if self.engine_on:
            self.engine_on=False
            print("The car engine has stopped!")
    def refuel(self, litr):
        self.fuel_level += int(litr)
        print(f"Refuelling with {litr} litres of fuel")
    def drive(self,km):
        if not self.engine_on:
            print("Please start the engine first")
            return
        if int(km)/10<=int(self.fuel_level):
            self.fuel_level -= int(km)/10
            print(f"Driving {km}km and used {int(km)/10}")
        else:
            print(f"current fuel level: {self.fuel_level}.\nYou need at least {int(km)/10} liters fuel. Please refuel first!")
    def display_info(self):
        print(f"Displaying updated info: \n{self.year} {self.color} {self.model} | Fuel-level: {self.fuel_level} | Engine: {'On' if self.engine_on else 'Off'} ")
        

my_car = Car("Black","Benz", 2025)
my_car.start_engine()
my_car.drive(800)
my_car.drive(300)
my_car.refuel(30)
my_car.drive(300)
my_car.stop_engine()
my_car.display_info()