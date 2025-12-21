import numpy as np

arr = np.array([1,2,3,4,5,6])

print(arr)
print(type(arr))
print(arr.shape)
arr = arr.reshape(1,1,3,2)
print(arr.shape)
print(arr)

print()

arr2 = np.array([1,2])
arr2 = arr2.reshape(1,2)
print(arr2)
print(type(arr2))
print(arr2.shape)