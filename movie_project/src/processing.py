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
    days_on_air: Series
        The number of days between the first and last air date for each show.
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
    df['homepage'].fillna('NOT AVAILABLE', inplace=True)
    df['poster_path'].fillna('NOT AVAILABLE', inplace=True)
    df['homepage'].replace('', 'NOT AVAILABLE', inplace=True)
    df['poster_path'].replace('', 'NOT AVAILABLE', inplace=True)

    show_poster_dict = OrderedDict(zip(df['name'], df['homepage'] + df['poster_path']))

    # Print the first 5 records
    # for i, (key, value) in enumerate(show_poster_dict.items()):
    #     if i > 4:
    #         break
    #     print(f"{key}: {value}")

    return show_poster_dict