import numpy as np 

arr = np.array([[1,2,3,4,5,6],
                [7,8,9,10,11,12],
                [13,14,15,16,17,18]])

print('Array:\n', arr)
print(arr[0][5])

print(arr[1:, 4:]) #extracting from 1st row and 4th column to create new array
# the output of arr[1:, 4:] will bw an array consiting elements from 1st row to last row and 4th column to last column

print(arr[:2,:2])