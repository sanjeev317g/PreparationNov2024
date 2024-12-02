

def errorHandling():
        try:
            number = 4
            if(number % 2 == 1):
                print("Number devisable by 2")
        except Exception as e:
            print(f"aaaaaaa{e}")
        finally:
             print("Normal")

# errorHandling()

def exception():
     try:
          if(4 / 2 == 9):
              print("This will not give result 9 ")
     except Exception as e:
          print(f"condition not satisfied {e}")
     finally:
          print("This how ")
exception()
     





            