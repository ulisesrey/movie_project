"""

Disclaimer:
============
Some of these functions are very simple, in some cases one-liners and might not need a function by itself.
But the purpose of these exercise was also in part to organize code in modules, so it made sense to do it like this.
"""

import pandas as pd


# function to filter by language
def filter_by_language(df, language, strict=True):
    """
    Filter the dataframe by language.

    Parameters:
    ------------
    df: DataFrame
        The dataframe to be filtered.
    language: str
        The language to filter by.
    strict: bool
        If True, the language must match exactly the language in the dataframe.
        If False, the language in the dataframe must contain the language.
            e.g.: if language = "ja" would return a row with language = "en, ja, ko"
            Attention:
            if language = "ja" meant for "japanese" would return a row with language="javanese"

    Returns:
    ------------
    filtered_df: DataFrame
        The filtered dataframe.
    """
    if strict:
        filtered_df = df[df["original_language"] == language]
    else:
        filtered_df = df[df["original_language"].str.contains(language, na=False, case=False)]

    return filtered_df

def filter_by_string_in_overview(df, strings_to_filter):
    """
    Filter the dataframe by string in overview.

    Parameters:
    ------------
    df: DataFrame
        The dataframe to be filtered.
    strings_to_filter: list
        The list of strings to filter by.

    Returns:
    ------------
    filtered_df: DataFrame
        The filtered dataframe.
    """
    # str.contains() should NOT be case sensitive
    filtered_df = df[df["overview"].str.contains('|'.join(strings_to_filter), na=False, case=False)]
    return filtered_df

def filter_by_starting_year(df, start_year):
    """
    Filter the dataframe by year.

    Parameters:
    ------------
    df: DataFrame
        The dataframe to be filtered.
    start_year: int
        The year to filter by.

    Returns:
    ------------
    filtered_df: DataFrame
        The filtered dataframe.
    """
    df["first_air_date"] = pd.to_datetime(df["first_air_date"])

    filtered_df = df[df["first_air_date"].dt.year == start_year]
    return filtered_df

def filter_by_status(df, status):
    """
    Filter the dataframe by status.

    Parameters:
    ------------
    df: DataFrame
        The dataframe to be filtered.
    status: str
        The status to filter by.

    Returns:
    ------------
    filtered_df: DataFrame
        The filtered dataframe.
    """
    filtered_df = df[df["status"] == status]
    return filtered_df

def filter_genres(df, minimum_percentage=0.01):
    """
    Filters genres that are below a threshold and removes movies without a genre.

    Parameters:
    ------------
    df: DataFrame
        The dataframe to be filtered.

    Returns:
    ------------
    filtered_df: DataFrame
        The filtered dataframe.
    """
    # drop rows where genres is Nan
    df.dropna(subset=["genres"], inplace=True)
    genres = df.groupby(by="genres")

    # get list of all genres TODO: This part could be improved
    genres_list = genres.size().index.to_list()
    flattened_list = [item for sublist in (s.split(',') for s in genres_list) for item in sublist]
    
    # remove spaces from list, to merge e.g. " Drama" and "Drama"
    flattened_list = [s.strip() for s in flattened_list]

    genres_count = pd.Series(flattened_list).value_counts()
    total_genres_count = genres_count.sum()
    genres_percent = genres_count/total_genres_count

    # filter genres that are below a threshold
    genres_to_keep = genres_percent[genres_percent > minimum_percentage].index.to_list()
    genres_to_discard = genres_percent[genres_percent <= minimum_percentage].index.to_list()


    genres_df = pd.DataFrame(genres_percent)
    genres_df.reset_index(inplace=True)
    genres_clean_df = genres_df.replace(genres_to_discard, "Other")
    # Combine all categories that now are "Other"
    combined_series = genres_clean_df.groupby('index')['count'].sum()
    

    #df[]

    return combined_series

