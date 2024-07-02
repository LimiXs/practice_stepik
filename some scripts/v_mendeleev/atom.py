import matplotlib.pyplot as plt
from mendeleev import element
import math


# Функция для получения электронных уровней
def get_electron_shells(electrons):
    shells = [2, 8, 18, 32, 32, 18, 8]  # Максимальные числа электронов на уровнях
    electron_distribution = []
    for shell in shells:
        if electrons > 0:
            electrons_in_shell = min(shell, electrons)
            electron_distribution.append(electrons_in_shell)
            electrons -= electrons_in_shell
        else:
            electron_distribution.append(0)
    return electron_distribution


# Функция для визуализации атома
def plot_atom(atomic_number):
    el = element(atomic_number)
    electron_shells = get_electron_shells(el.electrons)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Рисуем ядро
    ax.add_artist(plt.Circle((0, 0), 0.2, color='red', label='Nucleus'))
    ax.text(0, 0, el.symbol, color='white', fontsize=12, ha='center', va='center')

    # Рисуем электронные оболочки и электроны
    shell_radius = 1
    for i, electrons in enumerate(electron_shells):
        if electrons > 0:
            shell = plt.Circle((0, 0), shell_radius, color='black', fill=False)
            ax.add_artist(shell)
            for j in range(electrons):
                angle = 2 * math.pi * j / electrons
                x = shell_radius * math.cos(angle)
                y = shell_radius * math.sin(angle)
                ax.add_artist(plt.Circle((x, y), 0.05, color='blue'))
            shell_radius += 1

    plt.xlim(-shell_radius, shell_radius)
    plt.ylim(-shell_radius, shell_radius)
    plt.title(f'Атом {el.name} ({el.symbol}) - атомный номер {el.atomic_number}')
    plt.axis('off')
    plt.show()


# Основная программа
if __name__ == "__main__":
    atomic_number = int(input("Введите атомный номер элемента: "))
    plot_atom(atomic_number)
