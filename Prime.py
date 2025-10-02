value = int(input("Enter the range\n"))

for i in range(2, value + 1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
    if flag:
        print(i)