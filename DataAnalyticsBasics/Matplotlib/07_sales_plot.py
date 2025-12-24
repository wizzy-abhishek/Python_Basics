import pandas as pd 
import matplotlib.pyplot as plt 

file_path = "DataAnalyticsBasics/Matplotlib/sales.csv"

sales_df = pd.read_csv(file_path)
sales_df.drop_duplicates(inplace=True)

print(sales_df)

print('------------------------------------------------------------------------')
sales_by_product = sales_df.groupby('Category')['TotalAmount'].sum().reset_index()

print(sales_by_product)

plt.bar(sales_by_product['Category'],sales_by_product['TotalAmount'])
plt.show()

print('-------------------------------------------------------------------------')
sales_by_date = sales_df.groupby('OrderDate')['TotalAmount'].sum().reset_index()
print(sales_by_date)

plt.pie(sales_by_date['TotalAmount'], labels=sales_by_date['OrderDate'], autopct="%1.1f%%") 
plt.show()