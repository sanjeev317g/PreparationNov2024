from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def car(self):
        pass

class Vehicle1(Vehicle):
    def car(self):
         print("car methos from none abstract class")
    
    def car(self):
        print("Implemented abstract class methos under Vehicle1 class")
    
class Vehicle2(Vehicle):
    def car(self):
        print("Implemented abstract class method under Vehicle2 class")
    


def OutSideClass(vehicle: Vehicle):
    vehicle.car()

v1 = Vehicle1()
v2 = Vehicle2()

OutSideClass(v1)
OutSideClass(v2)
v1.car()
v2.car()