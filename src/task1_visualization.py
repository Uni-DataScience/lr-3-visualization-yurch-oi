import matplotlib.pyplot as plt
import numpy as np
import collections


def plot_distribution(data):
    """
    Plots the distribution of data using a bar chart.

    Parameters:
    data (array-like): An array of categorical data items.
    """
    
    fig, _ = plt.subplots()
    pass
    return fig


# Example data
data = np.random.choice(['A', 'B', 'C'], size=100)
plot_distribution(data)
