import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y1 = [100, 100, 100, 200, 300]
y2 = [1.2,1.5,1.8,99,-1]

plt.figure(figsize=(9,8))

plt.subplot(2,2,1)
plt.plot(x, y1, color='red')
plt.title("P1")


plt.subplot(2,2,2)
plt.plot(x, y2, color='blue')
plt.title("P2")


plt.subplot(2,2,3)
plt.plot(y2, y1, color='orange')
plt.title("P3")


plt.subplot(2,2,4)
plt.plot([y*2 for y in x], y1, color='yellow')
plt.title("41")

plt.show()