import matplotlib.pyplot as plt

data = [1,2,1,4,1,2,2,4,4,4,3,4,4,4]

plt.hist(data, bins = 4, color='orange', edgecolor= 'black')
plt.show()