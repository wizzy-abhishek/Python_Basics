import numpy as np

data = np.array([1,2,3,4])
print(np.mean(data))
print(np.median(data))
print(np.var(data))
print(np.std(data))

## Normalization of dataset

mean = np.mean(data)
std_dev = np.std(data)

normalized_data = (data - mean)/std_dev
print(normalized_data)