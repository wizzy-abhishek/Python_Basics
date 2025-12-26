import sys
import math
import multiprocessing

sys.set_int_max_str_digits(100000)

def factorial(num):
    return f"Factorial of {num} is {math.factorial(num)}"

numbers = [1000,2000,5000,9999]

if __name__ == '__main__':

    with multiprocessing.Pool() as pool:
        result = pool.map(factorial, numbers)
    
    print(result)