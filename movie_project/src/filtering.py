
# function to filter by language
def filter_by_language(df, language):
    """
    Filter the dataframe by language.

    Parameters:
    ------------
    df: DataFrame
        The dataframe to be filtered.
    language: str
        The language to filter by.

    Returns:
    ------------
    filtered_df: DataFrame
        The filtered dataframe.
    """
    filtered_df = df[df["original_language"] == language]
    return filtered_df

def filter_by_string_in_overview(df, list_of_strings):
    """
    Filter the dataframe by string in overview.

    Parameters:
    ------------
    df: DataFrame
        The dataframe to be filtered.
    list_of_strings: list
        The list of strings to filter by.

    Returns:
    ------------
    filtered_df: DataFrame
        The filtered dataframe.
    """
    # str.contains() should be case insensitive
    filtered_df = df[df["overview"].str.contains('|'.join(list_of_strings), case=False)]
    return filtered_df