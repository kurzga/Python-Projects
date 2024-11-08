import random
import matplotlib.pyplot as plt


def galton_board_simulation(rows, balls):
    slots = [0] * (rows + 1)

    for _ in range(balls):
        position = 0
        for _ in range(rows):
            direction = random.choice([0, 1])
            position = position + direction
        slots[position] = slots[position] + 1

    return slots


def plot_simulation(slots):
    plt.bar(range(len(slots)), slots)
    plt.title('Galton Board Simulation')
    plt.xlabel('Position')
    plt.ylabel('Number of Balls')


# 10 kez simülasyonu çalıştır ve her bir sonucu görselleştir
for i in range(10):
    rows = 10
    balls = 1000

    slots = galton_board_simulation(rows, balls)

    # Çubuk grafikleri aynı pencere üzerinde göstermek için 'subplot' kullanılır.
    plt.subplot(2, 5, i + 1)
    plot_simulation(slots)

plt.tight_layout()
plt.show()
