var = input("Enter any string\n")
new = ""
for i in range(len(var) -1, -1, -1):
    new += var[i]

print(new)