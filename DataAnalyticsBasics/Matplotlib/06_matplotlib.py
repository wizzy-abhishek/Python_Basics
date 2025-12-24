import matplotlib.pyplot as pl

label = ['A', 'B', 'C', 'D']
size = [124,26,31,19]
color=['gold', 'green', 'grey', 'lightcoral']
explode = [0.2,0,0,0.1]

pl.pie(size, labels=label, colors=color, explode=explode, autopct="%1.1f%%")
pl.show()