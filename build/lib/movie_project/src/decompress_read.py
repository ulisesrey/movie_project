import os
import zipfile
import tarfile
import pandas as pd
import time
import csv

import os
import zipfile
import tarfile

def decompress_file(file_path, output_dir=None):
    """
    Decompress a tar.gz or .zip file given its path
    Parameters:
    ------------
    file_path: str
        The path of the input file (.zip or .tar.gz).
    output_dir: str, optional
        The directory where the contents should be extracted. If not provided, it defaults to the directory of the input file.
    """
    file_extension = os.path.splitext(file_path)[1]
    
    # Set the default extraction directory to the directory of the input file
    extract_dir = output_dir or os.path.dirname(file_path)

    if file_extension == '.zip':
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)  # Extract in the specified or default directory
        print(f"File {file_path} has been successfully decompressed.")
    elif file_extension == '.tar.gz':
        with tarfile.open(file_path, 'r:gz') as tar_ref:
            tar_ref.extractall(extract_dir)  # Extract in the specified or default directory
        print(f"File {file_path} has been successfully decompressed.")
    else:
        print(f"Error: File {file_path} is not in zip or tar.gz format.")


def read_and_merge_csv(csv_list, id="id"):
    """
    Read multiple CSV files and merge them into a single DataFrame using the specified key.

    Parameters:
    ------------
    csv_list: list
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

    dfs = (pd.read_csv(csv_file) for csv_file in csv_list)
    merged_df = pd.concat(dfs, ignore_index=True)

    # merged_df.set_index(id, inplace=True)
    end_time = time.time()
    print(f"Processing time: {end_time - start_time} seconds")

    return merged_df


def read_and_merge_csv_to_dict(csv_list, id="id"):
    """
    Read multiple CSV files and merge them into a single dictionary using the specified key.

    Parameters:
    ------------
    csv_list: list
        A list of paths to the CSV files to be read and merged.
    id: str, optional
        The column name to use as the key for merging the dictionaries. Default is "id".

    Returns:
    ------------
    merged_dict: dict
        The merged dictionary.
    """
    start_time = time.time()
    merged_dict = {}

    for csv_file in csv_list:
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                merged_dict[row[id]] = row

    end_time = time.time()
    print(f"Processing time: {end_time - start_time} seconds")

    return merged_dict

# Example usage
#decompress_file('/path/to/TMDB.zip')
