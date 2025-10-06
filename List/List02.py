list = []

val = int(input("Enter the number of items you want to put in list\n"))
print(f"Enter {val} numbers:\n")

for i in range(val):
    list.append(int(input(f"Enter {i} value: ")))

print(list)