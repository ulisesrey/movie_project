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

def plot_type_per_decade(df, start_decade=1940, normalize=True):
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

    counts_per_decade = df.groupby(["decade","type"]).size().unstack()
    if normalize:
        counts_per_decade = counts_per_decade.div(counts_per_decade.sum(axis=1), axis=0)
    
    counts_per_decade.plot(kind="bar", stacked=True)
    plt.title('Types of shows per decade')
    plt.ylabel("Percentage of shows")
    plt.show()


def genre_piechart(series):
    """
    Plot a piechart with the percentage of shows per genre.

    Parameters:
    ------------
    series: pd.Series
        
    Returns:
    ------------
    None
    """
    #do a piechart with the series, title should be "Piechart of genres"
    _, labels, pct_texts = plt.pie(series, autopct='%1.1f%%',\
                                labels=series.index, rotatelabels=True, labeldistance=1.1,\
                                pctdistance=0.8)
    for label, pct_text in zip(labels, pct_texts):
        pct_text.set_rotation(label.get_rotation())

    plt.title('Shows per genre', loc="left")
    plt.show()
    