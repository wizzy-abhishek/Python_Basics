import pandas as pd

data = ['1',2,3,4]
series = pd.Series(data)
print(series)


data = [10,20,30,40]
index = ['a', 'g', 'a','b']
series = pd.Series(data, index, verify_integrity=True)

print(series)