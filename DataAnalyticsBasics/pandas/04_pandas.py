import pandas as pd

file_path = 'DataAnalyticsBasics/pandas/sales.csv'

data_file = pd.read_csv(file_path)

print(data_file.head(4)) # Gives first 4 record
print()
print(data_file.tail(4)) # Gives last 4 record

cost_price = data_file['UnitPrice']
cost_price = [cp - cp*0.1 for cp in cost_price]
data_file['Cost_price'] = cost_price

print()
data_file.drop('SalesPerson',axis=1, inplace=True)
print(data_file)


file_path2 = 'DataAnalyticsBasics/pandas/sales2.csv'
data_file2 = pd.read_csv(file_path2)

data_file2.drop('SalesPerson', axis=1, inplace= True)
cost_price = data_file2['UnitPrice']
cost_price = [cp - cp*0.1 for cp in cost_price] # Mistake I have not added this column to data_file 2, but it shows NaN
data_file = pd.concat([data_file, data_file2], ignore_index=True)
print()
print(data_file)

"""
This is the basic of data manipulation, I will create a fucntion to streamline process
"""
