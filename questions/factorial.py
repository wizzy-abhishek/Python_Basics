val = int(input("Enter the number for which you want factorial\n"))

factorial = 1

for i in range(1, val + 1):
    factorial *= i 

print(factorial)