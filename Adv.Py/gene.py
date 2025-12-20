def squares(num):
    for i in range(num + 1):
        print(f"In squares, for value {i}")
        yield i**2

user = int(input("Enter any number\n"))

for i in squares(user):
    print(f"Not in func:: {i}")