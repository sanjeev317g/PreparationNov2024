class StaticClassSuperMethods:

    @staticmethod
    def staicmethods():
        print("This is a staic method")
    
    @classmethod
    def classmethod(cls):
        print("This is a class method")
    
StaticClassSuperMethods.staicmethods()
StaticClassSuperMethods.classmethod()