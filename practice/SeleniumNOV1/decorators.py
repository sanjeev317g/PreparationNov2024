
def addition(func):
    def addition1():
        print("Decorators")
        a = 5
        b = 10
        c = a +b
        result = func("Test")
        print(a+5)
        return result
    return  addition1
    
@addition
def callDecorator(c):
    print(f"First DEcorator will get executed, and then the linkes mentioned here+ {c}")
    return  c

callDecorator()

