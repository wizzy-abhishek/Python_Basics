import time
print("This is the dividing calculator")
time.sleep(2)
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(num1/num2)
except ValueError as ex:
    print(ex)
except ZeroDivisionError as ex:
    print(ex)
except Exception as ex:
    print(ex)