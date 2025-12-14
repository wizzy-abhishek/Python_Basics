def odd(num):
    if num % 2 != 0:
        return num

numbers=[1,2,4,5,56,7,8,8,99,7]

odd_numbers= list(map(odd, numbers))

print(odd_numbers)

## Filter to remove none, I know this could be done in one line I am just trying 

odd_numbers = tuple(filter(lambda x: x != None, odd_numbers))

print(odd_numbers)