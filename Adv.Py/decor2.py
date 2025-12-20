
def decorator(func):
    def wrapper(num):
        return func(num)
    return wrapper


@decorator
def factorial(num):
    if num <= 1: 
        return 1
    return num * factorial(num-1)

print(factorial(5))