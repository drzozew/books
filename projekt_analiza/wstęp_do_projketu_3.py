import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)

# zdefiniowanie tytułu wykresu i etykiety osi.
ax.set_title("Kwadrat liczby", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# zdefiniowanie wielkości etykiety
ax.axis([0, 1100, 0, 1100000])

plt.show()
