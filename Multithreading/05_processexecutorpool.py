from concurrent.futures import ProcessPoolExecutor
import time
import math

def findNumberOfPrimes(num):
    count = 0
    for j in range(2,num):
        if isPrime(j):
            count += 1
    return f"The number of prime between 1 and {num} is {count}"

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
        
numbers = [300_000, 400_000, 500_000, 600_000]

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=7) as exe:
        res = exe.map(findNumberOfPrimes,numbers)

    for r in res:
        print(r)
    
    exe.shutdown()