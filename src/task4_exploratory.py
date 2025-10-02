import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def perform_eda(df):
    """
    Performs EDA including descriptive statistics, outlier detection,
    and correlation analysis.

    Parameters:
    df (DataFrame): A DataFrame containing data for EDA.
    """

    # === 1. Descriptive statistics ===
    desc_stats = pd.DataFrame({
        'mean': df.mean(),
        'median': df.median(),
        'mode': df.mode().iloc[0],
        'variance': df.var(),
        'std_dev': df.std(),
        'min': df.min(),
        'max': df.max()
    })

    print("\n=== Descriptive Statistics ===")
    print(desc_stats)

    # === 2. Boxplot for outlier detection ===
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df)
    plt.title("Boxplot for Outlier Detection")
    plt.show()

    # === 3. Correlation matrix and heatmap ===
    corr_matrix = df.corr()

    plt.figure(figsize=(6, 5))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()

    # Explanation of findings
    print("\n=== Findings ===")
    print("1. Descriptive statistics summarize the central tendency, dispersion, and range of each feature.")
    print("2. Boxplots help to identify potential outliers and visualize data distribution.")
    print("3. The correlation heatmap shows linear relationships between variables.")


# Приклад використання
if __name__ == "__main__":
    df = pd.DataFrame({
        'A': np.random.rand(50),
        'B': np.random.rand(50) * 10,
        'C': np.random.rand(50) * 100
    })
    perform_eda(df)
