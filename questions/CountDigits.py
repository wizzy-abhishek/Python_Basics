var = int(input("Enter any number\n"))
count = 0

while var > 0 :
    count += 1
    var = var // 10 
    """ 
    / is used for float division 
    // is used for integer divison
    """

print(count)