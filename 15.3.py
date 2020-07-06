import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Przygotowanie danych błądzenia losowego i wyświetlenie punktów.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Wyświetlenie punktów błądzenie losowego.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=2)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_runung = input("Utworzyć kolejen błądzenie losowe? (t/n):")
    if keep_runung == 'n':
        break
