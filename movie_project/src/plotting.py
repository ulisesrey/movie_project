"""
Module to plot data

Disclaimer:
In some cases the plt.show() might need to be set to plt.show(block=True) to see the plot.
ref:
https://stackoverflow.com/questions/36269746/matplotlib-plots-arent-shown-when-running-file-from-bash-terminal
"""


import matplotlib.pyplot as plt
import pandas as pd

def plot_count_per_year(df):
    """
    Plot the number of shows per year.

    Parameters:
    ------------
    df: DataFrame
        The dataframe containing the air dates.

    Returns:
    ------------
    None
    TODO: return fig? add a save_fig parameter?
    """
    df["first_air_date"] = pd.to_datetime(df["first_air_date"])
    df["first_air_date"].dt.year.value_counts().sort_index().plot(kind="bar")
    plt.title("Number of shows per year")
    plt.xlabel("Year")
    plt.ylabel("Number of shows")
    plt.show() 
    return None