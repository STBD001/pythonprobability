import matplotlib.pyplot as plt
import random
import statistics

try:
    n = int(input('Podaj liczbę rzutów: '))
    sides = int(input('Podaj liczbę ścian: '))
except ValueError:
    print("Proszę podać prawidłowe liczby całkowite.")
    exit()

def roll_dice(sides):
    return random.randint(1, sides)

def simulate_rolls(n, sides):
    rolls = [roll_dice(sides) for _ in range(n)]
    return rolls

def plot_histogram(rolls, sides):
    plt.hist(rolls, bins=range(1, sides + 2), edgecolor='black', align='left', rwidth=0.8)
    plt.title(f'Rozkład rzutów kostką {sides}-ścienną')
    plt.xlabel('Wyniki')
    plt.ylabel('Liczba wystąpień')
    plt.xticks(range(1, sides + 1))
    plt.show()

rolls = simulate_rolls(n, sides)
plot_histogram(rolls, sides)

def analyze_rolls(rolls):
    print(f"Średnia: {statistics.mean(rolls)}")
    print(f"Mediana: {statistics.median(rolls)}")
    print(f"Moda: {statistics.mode(rolls)}")
    print(f"Wariancja: {statistics.variance(rolls)}")

analyze_rolls(rolls)

def simulate_multiple_series(series_count, n, sides=6):
    all_rolls = []
    for i in range(series_count):
        rolls = simulate_rolls(n, sides)
        all_rolls.append(rolls)
        print(f"Seria {i+1}:")
        analyze_rolls(rolls)
        plot_histogram(rolls, sides)

series_count = int(input("Podaj liczbę serii: "))
simulate_multiple_series(series_count, n, sides)

def simulate_multiple_dice_rolls(n, dice_count=2, sides=6):
    rolls = [sum(roll_dice(sides) for _ in range(dice_count)) for _ in range(n)]
    return rolls

dice_count = int(input("Podaj liczbę kostek: "))
rolls = simulate_multiple_dice_rolls(n, dice_count, sides)
plot_histogram(rolls, sides * dice_count)