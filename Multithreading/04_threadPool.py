from concurrent.futures import ThreadPoolExecutor
import time

def print_n(nums):
    time.sleep(5)
    return nums

numbers = [1,2,4,5,6,6,3,2,2,3,4,5,4,32,4444,22,1,9786,1,2,3,4,4,45,454,886434]

with ThreadPoolExecutor(max_workers=10) as executor:
    result = executor.map(print_n, numbers)

print(result) # <generator object Executor.map.<locals>.result_iterator at 0x1033631f0>

for r in result:
    print(r)