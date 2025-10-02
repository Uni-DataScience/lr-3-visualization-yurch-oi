import seaborn as sns
import matplotlib.pyplot as plt

def create_scatter_plot(data):
    """
    Creates a scatter plot using Seaborn.

    Parameters:
    data (DataFrame): A DataFrame containing 'x' and 'y' columns.

    Returns:
    fig (matplotlib.figure.Figure): The generated scatter plot figure.
    """
    # Використовуємо стиль Seaborn для простоти і зрозумілості
    sns.set(style="whitegrid")

    # Створюємо фігуру та осі
    fig, ax = plt.subplots(figsize=(6, 4))

    # Будуємо scatter plot
    sns.scatterplot(data=data, x='x', y='y', ax=ax)

    # Додаємо підписи та заголовок
    ax.set_xlabel("X values", fontsize=12)
    ax.set_ylabel("Y values", fontsize=12)
    ax.set_title("Scatter Plot of X vs Y", fontsize=14)

    # Додаємо сітку для кращої читаємості
    ax.grid(True, linestyle="--", alpha=0.7)

    return fig
