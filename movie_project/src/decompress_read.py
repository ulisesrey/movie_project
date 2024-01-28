"""
TODO: add docstring
"""

import os
import zipfile
import tarfile
import pandas as pd
import time
import csv

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
        print(f"File {file_path} has been successfully decompressed in: ", extract_dir)
    elif file_extension == '.tar.gz':
        with tarfile.open(file_path, 'r:gz') as tar_ref:
            tar_ref.extractall(extract_dir)  # Extract in the specified or default directory
        print(f"File {file_path} has been successfully decompressed in: ", extract_dir)
    else:
        print(f"Error: File {file_path} is not in zip or tar.gz format.")


def read_and_merge_csv_files(csv_files, id="id"):
    """
    Merge multiple CSV files into a single DataFrame based on the 'ID' column.

    Parameters:
    - csv_files (list): List of paths to CSV files.

    Returns:
    - pd.DataFrame: Merged DataFrame.
    """

    start_time = time.time()
    
    # Initialize an empty DataFrame
    merged_df = pd.DataFrame()

    # Iterate through each CSV file
    for i, csv_file in enumerate(csv_files):
        # Read the CSV file
        df = pd.read_csv(csv_file)
        if i == 0:
            # If it's the first CSV file, assign it to the DataFrame
            merged_df = df
        else:
            # Merge with the existing DataFrame based on the 'ID' column
            merged_df = pd.merge(merged_df, df, on='id', how="outer")
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

