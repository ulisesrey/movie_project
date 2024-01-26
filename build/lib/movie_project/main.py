import glob
from src.decompress_read import *


if __name__ == "__main__":
    
    # decompress the compressed file
    #decompress_file("data/TMDB.zip", "data/")

    # get the list of csv files
    csv_list = glob.glob("data/*.csv")

    # merge the csv files into a single dataframe
    merged_df = read_and_merge_csv(csv_list, id="id")
    print(len(merged_df))
    # merge the csv files into a single dictionary
    merged_dict = read_and_merge_csv_to_dict(csv_list, id="id")