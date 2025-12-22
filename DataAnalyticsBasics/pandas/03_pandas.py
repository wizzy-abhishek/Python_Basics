import pandas as pd

data = [
    {'Name':'Abhishek Anand', 'Age': 21, 'City': 'Sultanganj'},
    {'Name':'Gragi Parmar', 'Age': 21, 'City': 'Bhopal'},
    {'Name':'Bubu Dudu', 'Age': 32, 'City': 'Dholakpur'},
]

df = pd.DataFrame(data)

ele = df.iloc[0]
print(ele)

print(df[['Name', 'Age']]) # PASSING a LIST of ATTRIBUTES to get those values