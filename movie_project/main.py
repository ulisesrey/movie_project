import glob
from movie_project.src.decompress_read import *
from movie_project.src.processing import calculate_days_on_air
from movie_project.src.processing import create_show_poster_dict

if __name__ == "__main__":
    
    # decompress the compressed file
    #decompress_file("movie_project/data/TMDB.zip", "movie_project/data/")

    # get the list of csv files
    csv_list = glob.glob("movie_project/data/*.csv")

    # merge the csv files into a single dataframe
    merged_df = read_and_merge_csv_files(csv_list, id="id")
    # optional to save the merged_df
    merged_df.to_csv("movie_project/reports/data/merged_df.csv", index=False)

    # # merge the csv files into a single dictionary
    merged_dict = read_and_merge_csv_to_dict(csv_list, id="id")
    len(merged_dict)

    # Answer to Exercise 1.4:
    print("blabla bla")


    # Exercise 2:
    ## Exercise 2.1:
    days_on_air = calculate_days_on_air(merged_df)

    # Show top 10 shows with the most days on air
    days_on_air.sort_values(by="days_on_air", ascending=False).head(10)

    ## Exercise 2.2:
    # Create a dictionary with show names and poster paths
    poster_dict = create_show_poster_dict(merged_df)

    # Show the first 5 shows in the dictionary
    for key, value in list(poster_dict.items())[:5]:
        print(f"{key}: {value}")

    print("THE END")