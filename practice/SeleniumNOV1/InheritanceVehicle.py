class Vehicle:
    def __init__(self):
        # self.brand = brand
        print(f"Creating any object a constructor will be call Mahesh underwares")

    def anvesh(self):
        print("Anvesh Baniyan")


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("from child class")
    def teja(self):
        print("Teja Dyppers")
        # super()

car = Car()
car.anvesh()
car.teja()

    

        