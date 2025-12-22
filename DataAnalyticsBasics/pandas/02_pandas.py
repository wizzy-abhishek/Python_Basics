import pandas as pd
import numpy as np 

data = {
    'name':['Abhishek', 'Gargi', 'Bubu', 'Dudu'],
    'age':[21,21,44,44],
    'city':['Sultanganj', 'Bhopal', 'Dholakpur', 'Dholakpur']
}

data_frame = pd.DataFrame(data)
print('\n',data_frame)

data_array = np.array(data_frame)
print('\n',data_array)

data = [
    {'Name':'Abhishek Anand', 'Age': 21, 'City': 'Sultanganj'},
    {'Name':'Gragi Parmar', 'Age': 21, 'City': 'Bhopal'},
    {'Name':'Bubu Dudu', 'Age': 32, 'City': 'Dholakpur'},
]

data_frame = pd.DataFrame(data)
print('\n',data_frame)