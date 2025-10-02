import numpy as np
import matplotlib.pyplot as plt
import collections


def plot_distribution(data):
    """
    Plots the distribution of data using a bar chart.

    Parameters:
    data (array-like): An array of categorical data items.
    Returns:
    fig (matplotlib.figure.Figure): The created matplotlib figure.
    """
    # Підрахунок частот
    counter = collections.Counter(data)
    categories = list(counter.keys())
    counts = list(counter.values())

    # Побудова графіка
    fig, ax = plt.subplots()
    ax.bar(categories, counts, color=['skyblue', 'lightgreen', 'salmon'], edgecolor='black')
    ax.set_xlabel("Category")
    ax.set_ylabel("Frequency")
    ax.set_title("Frequency Distribution of Categories")

    return fig


if __name__ == "__main__":
    # Генеруємо випадковий набір категорій A, B, C
    data = np.random.choice(['A', 'B', 'C'], size=100)

    # Будуємо розподіл
    fig = plot_distribution(data)
    plt.show()
