def fibonacciSeries():
    number = 20;
    num1 = 0;
    num2 = 1;
    num3 = 0;
    for n in range(number):
        num3 = num1 + num2;
        print(num3)
        num1 = num2;
        num2 = num3;

            
fibonacciSeries()
