import glob
from src.decompress_read import *
from movie_project.src.processing import calculate_days_on_air
if __name__ == "__main__":
    
    # decompress the compressed file
    #decompress_file("movie_project/data/TMDB.zip", "movie_project/data/")

    # get the list of csv files
    csv_list = glob.glob("movie_project/data/*.csv")

    # merge the csv files into a single dataframe
    merged_df = read_and_merge_csv_files(csv_list, id="id")
    # optional to save the merged_df
    merged_df.to_csv("movie_project/data/merged_df.csv", index=False)

    # # merge the csv files into a single dictionary
    merged_dict = read_and_merge_csv_to_dict(csv_list, id="id")
    len(merged_dict)

    

    # Exercise 2:
    ## Exercise 2.1:
    days_on_air = calculate_days_on_air(merged_df)

    days_on_air.head()