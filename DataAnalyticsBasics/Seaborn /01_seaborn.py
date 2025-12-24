import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

file_path = "DataAnalyticsBasics/Seaborn /food_bills.csv"
#### dataset = sb.load_dataset('tips') # Reads data from urls

dataset = pd.read_csv(file_path)
print(dataset)
print("------------------------------------------------------------")

sb.scatterplot(x=dataset['age'], y= dataset['tip'], data=dataset)
plt.xlabel("AGE")
plt.ylabel("TIP")
plt.title("AGE v/s TIP")
plt.show()


sb.barplot(x = dataset['customer_sex'], y = dataset['food_category'], data= dataset)
plt.xlabel("customer_sex")
plt.ylabel("food_category")
plt.title("customer_sex v/s food_category")
plt.show()

sb.kdeplot(x=dataset['total_amt'],fill=True)
plt.show()

sb.pairplot(dataset)
plt.show()