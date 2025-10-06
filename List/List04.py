list = [sq**2 for sq in range(1, 11)]
print(list)

list2 = [even_number for even_number in list if even_number % 2 == 0]
print(list2)