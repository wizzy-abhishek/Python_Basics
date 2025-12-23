import matplotlib.pyplot as pl

x_axis = [1,2,4,8,16]
y_axis = [1,4,16,64,144]

pl.xlabel("X Axis")
pl.ylabel("Y Axis")
pl.title("Line plot")
pl.plot(x_axis, y_axis, color='blue', linestyle=':', marker='o', markersize = 4, linewidth=2)
pl.show()