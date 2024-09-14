import numpy as np

from src.task3_plotting import plot_1d, plot_2d, plot_3d


def test_plots():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    z = np.cos(x)

    try:
        plot_1d(x)
        print("1D plot generated successfully.")
    except Exception as e:
        assert False, f"1D plot generation failed with error: {e}"

    try:
        plot_2d(x, y)
        print("2D scatter plot generated successfully.")
    except Exception as e:
        assert False, f"2D plot generation failed with error: {e}"

    try:
        plot_3d(x, y, z)
        print("3D scatter plot generated successfully.")
    except Exception as e:
        assert False, f"3D plot generation failed with error: {e}"


test_plots()
