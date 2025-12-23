import pandas as pd

def sales_processed_data(filepath, columns_removed):
    data_file = pd.read_csv(filepath)
    data_file.drop_duplicates(inplace=True)
    data_file.drop(labels=columns_removed, axis=1, inplace=True)

    # For now I am assuming the cols UnitPrice and Qunatity will be non NaN 
    data_file['TotalAmount'] = (data_file['TotalAmount']
                                .fillna(data_file['UnitPrice'] * data_file['Quantity'])
                                .astype(int))
    return data_file

file_path1 = 'DataAnalyticsBasics/pandas/sales.csv'
file_path2 = 'DataAnalyticsBasics/pandas/sales2.csv'
columns_to_be_removed = ['SalesPerson', 'OrderID']

def concat_files(*filepaths):
    dfs = [sales_processed_data(file, columns_to_be_removed) for file in filepaths]
    final_df = pd.concat(dfs, ignore_index=True)
    return final_df

file = concat_files(file_path1, file_path2)
print(file)
# file.to_excel('final_sales.xlsx')

"""Area-wise sales"""
print('-----------------------------------------------------------')

area_wise_sales = file.groupby('City')['TotalAmount'].sum()
print(area_wise_sales)

print('-----------------------------------------------------------')
group = ['City', 'Category', 'Product']
product_category_area_sale = file.groupby(group)['TotalAmount'].sum()
print(product_category_area_sale)