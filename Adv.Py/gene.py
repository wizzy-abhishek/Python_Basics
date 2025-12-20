def squares(num):
    for i in range(num + 1): 
        print(f"In squares, for value {i}")
        yield i**2 # The value is produced one by one, then given to the caller and then if the callers it again the next value is generated 

user = int(input("Enter any number\n"))

for i in squares(user): # This loop just gets the next value to the function, and then returns the control to the function 
    print(f"Not in func:: {i}")