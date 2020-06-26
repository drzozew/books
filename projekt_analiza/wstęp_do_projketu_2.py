import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
input_values = [1, 2, 3, 4, 5]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# zdefinowanie tytułu wykresu i etykiet osi.
ax.set_title("Kwadrat liczby", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# zdefiniowanie wielkości etykiety.
ax.tick_params(axis='both', labelsize=14)

plt.show()
