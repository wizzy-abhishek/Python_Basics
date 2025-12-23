import matplotlib.pyplot as plt

categories = ['A','B','C']
values = [1,2,-1]

plt.bar(categories, values, color='cyan')
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar graph")
plt.show()