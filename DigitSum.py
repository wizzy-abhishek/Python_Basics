var = int(input("Enter any number\n"))

sum = 0

while var > 0:
    val = var % 10
    sum += val
    var = var // 10

print(sum)