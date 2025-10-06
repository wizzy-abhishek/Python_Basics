list = ["Abhishek", "Anand", "is", "the", "Best", "Best"]
c = list.count("Abhishek")
print(c)
print(list[::-2])

for i, word in enumerate(list):
    if i % 2 == 0:
        print(i, word)

### List comprehension with condition

sq_numbers = [num**2 for num in range(10) if num % 2 == 0]
print(sq_numbers)