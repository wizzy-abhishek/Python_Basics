var = int(input("Enter any number\n"))

reversedNum = 0

while var > 0:
    val = var % 10
    reversedNum = reversedNum*10 + val
    var = var//10

print(reversedNum)