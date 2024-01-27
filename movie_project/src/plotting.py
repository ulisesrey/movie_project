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

def plot_type_per_decade(df, start_decade=1940):
    """
    Plot the number of shows per genre and per decade.

    Parameters:
    ------------
    df: DataFrame
        The dataframe containing the air dates.

    Returns:
    ------------
    None
    """
    # If first_aire_date column is not datetype, convert it to datetype
    if df["first_air_date"].dtype != "datetime64[ns]":
        df["first_air_date"] = pd.to_datetime(df["first_air_date"])

    # create column "decade"
    df["decade"]=df["first_air_date"].dt.year//10*10
    df=df[df["decade"]>start_decade]
    df.groupby(["decade","type"]).size().unstack().plot(kind="bar")
    plt.show()
    return None


def genre_piechart(df):
    """
    Plot a piechart with the percentage of shows per genre.

    Parameters:
    ------------
    df: DataFrame
        
    Returns:
    ------------
    None
    """
    #do a piechart with the dataframe
    plt.pie(df.groupby("genres").size(), labels=df.groupby("genres").size().index, autopct='%1.1f%%')
    plt.show()
    return None
    