import matplotlib.pyplot as plt
from mendeleev import element


# Функция для получения данных об элементах
def get_elements_data():
    elements_data = []
    for i in range(1, 119):  # элементы от 1 до 118
        el = element(i)
        elements_data.append((el.name, el.atomic_number, el.atomic_weight))
    return elements_data


# Функция для визуализации данных
def plot_elements_data(elements_data):
    atomic_numbers = [data[1] for data in elements_data]
    atomic_weights = [data[2] for data in elements_data]

    plt.figure(figsize=(12, 6))
    plt.scatter(atomic_numbers, atomic_weights, color='blue', edgecolors='w', s=100)
    plt.title('Атомные веса элементов в зависимости от атомного номера')
    plt.xlabel('Атомный номер')
    plt.ylabel('Атомный вес')
    plt.grid(True)

    for data in elements_data:
        plt.text(data[1], data[2], data[0], fontsize=9, ha='right')

    plt.show()


# Основная программа
if __name__ == "__main__":
    elements_data = get_elements_data()
    plot_elements_data(elements_data)
