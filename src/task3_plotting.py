import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_1d(data):
    plt.figure()
    plt.plot(data, label="Values")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("1D Line Plot")
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_2d(x, y):
    plt.figure()
    plt.scatter(x, y, c="blue", marker="o")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("2D Scatter Plot")
    plt.grid(True)
    plt.show()


def plot_3d(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(x, y, z, c="red", marker="o")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_title("3D Scatter Plot")
    plt.show()


# Example data
if __name__ == "__main__":
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    z = np.cos(x)

    plot_1d(x)
    plot_2d(x, y)
    plot_3d(x, y, z)
