class MagicMethods:

    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"{self.name},{self.age} years old")

    def __repr__(self):
        return f"Person(name={self.name},age={self.age})"

mm = MagicMethods("Chaitanys", 30)

print(mm)