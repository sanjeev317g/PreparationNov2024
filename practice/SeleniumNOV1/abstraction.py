from abc import ABC,abstractmethod

class Vehicle:
    @abstractmethod
    def engine(self):
        pass


class Car(Vehicle):
    def engines(self):
        print("Engines")
    
    def engine(self):
        print("abstract file")

c = Car()
c.engine()