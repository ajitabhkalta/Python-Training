class Vehicle():
    def __init__(self,color,year,no_of_wheels):
        self.color=color
        self.year=year
        self.wheels=no_of_wheels
    def getVehicleInfo(self):
        return f"A {self.color} color vehicle with {self.wheels} wheels \
manufactured in {self.year}"

class TwoWheeler(Vehicle):
     def __init__(self,color,year,num_wheels,make,hp):
         super().__init__(color,year,num_wheels) #call parent class constructor 
         self.make=make
         self.hp=hp
     def getTwoWheelerInfo(self):
         print(super().getVehicleInfo())
         return f"Two wheeler is made by {self.make} that has {self.hp}"

obj1=TwoWheeler("black","2018","2","Bajaj","200cc")
print(obj1.getTwoWheelerInfo())
