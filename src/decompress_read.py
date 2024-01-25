import os
import zipfile
import tarfile
import time

def decompress_file(file_path):
    """
    Decompress a tar.gz or .zip file given its path
    Parameters:
    ------------
    file_path: str
    """
    file_extension = os.path.splitext(file_path)[1]

    if file_extension == '.zip':
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall()
        print(f"File {file_path} has been successfully decompressed.")
    elif file_extension == '.tar.gz':
        with tarfile.open(file_path, 'r:gz') as tar_ref:
            tar_ref.extractall()
        print(f"File {file_path} has been successfully decompressed.")
    else:
        print(f"Error: File {file_path} is not in zip or tar.gz format.")


def read_and_merge_csv(list_of_csvs, id="id"):
    """
    Read multiple CSV files and merge them into a single DataFrame using the specified key.

    Parameters:
    ------------
    list_of_csvs: list
        A list of paths to the CSV files to be read and merged.
    id: str, optional
        The column name to use as the key for merging the dataframes. Default is "id".

    Returns:
    ------------
    merged_df: DataFrame
        The merged dataframe.
    """
    start_time = time.time()
    merged_df = pd.DataFrame()

    for csv_file in list_of_csvs:
        df = pd.read_csv(csv_file)
        merged_df = pd.concat([merged_df, df], ignore_index=True, sort=False)

    merged_df.set_index(id, inplace=True)
    end_time = time.time()
    print(f"Processing time: {end_time - start_time} seconds")

    return merged_df


# Example usage
decompress_file('/path/to/TMDB.zip')

