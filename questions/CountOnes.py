val = input("Enter value\n")
target = input("Enter target character\n")
count = 0

for i in val:
    if i == target:
        count += 1

print(count)