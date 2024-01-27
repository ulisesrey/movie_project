import pandas as pd
from collections import OrderedDict

# add a function to convert df col to datetime?


def calculate_days_on_air(df):
    """
    Calculate the number of days between the first and last air date for each show.

    Parameters:
    ------------
    df: DataFrame
        The dataframe containing the air dates.

    Returns:
    ------------
    days_on_air: DataFrame
        Dataframe with the show id, name and number of days on air.
    """
    df["first_air_date"] = pd.to_datetime(df["first_air_date"])
    df["last_air_date"] = pd.to_datetime(df["last_air_date"])
    df["days_on_air"] =  df["last_air_date"] - df["first_air_date"]

    return df[["id","name","days_on_air"]]


def create_show_poster_dict(df):
    """
    Create an ordered dictionary where the key is the show name and the value is the full web address of its poster.

    Parameters:
    ------------
    df: DataFrame
        The dataframe containing the show names and poster paths.

    Returns:
    ------------
    show_poster_dict: OrderedDict
        The ordered dictionary with show names and poster paths.
    """

    #df.loc[:,('homepage', 'poster_path')].fillna('NOT AVAILABLE', inplace=True)
    #df.loc[:,('homepage', 'poster_path')].replace('', 'NOT AVAILABLE', inplace=True)
    df['homepage'].fillna("Not Available", inplace=True)
    df['homepage'].replace("", "Not Available", inplace=True)
    df['poster_path'].fillna("Not Available", inplace=True)
    df['poster_path'].replace("", "Not Available", inplace=True)

    df["full_poster_path"]=df["homepage"] + df["poster_path"]

    show_poster_dict = OrderedDict(zip(df['name'], df['full_poster_path']))

    return show_poster_dict