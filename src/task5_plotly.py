import numpy as np
import pandas as pd
import plotly.express as px
from plotly.graph_objects import Figure


def create_interactive_plotly(df):
    """
    Creates an interactive scatter plot using Plotly.

    Parameters:
    df (DataFrame): A DataFrame containing 'x' and 'y' columns.

    Returns:
    fig (plotly.graph_objects.Figure): Interactive scatter plot figure.
    """
    fig = px.scatter(
        df,
        x="x",
        y="y",
        title="Interactive Scatter Plot with Plotly",
        labels={"x": "X Axis", "y": "Y Axis"},
    )
    fig.update_layout(
        legend_title="Legend",
        hovermode="closest"
    )
    return fig


# Example usage
if __name__ == "__main__":
    df = pd.DataFrame({'x': np.random.rand(50), 'y': np.random.rand(50)})
    fig = create_interactive_plotly(df)
    fig.show()
