import matplotlib.pyplot as plt

x_values = [x**3 for x in range(1, 6)]
y_values = range(1, 6)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=50, c='red')
ax.plot(x_values, y_values)


plt.show()
