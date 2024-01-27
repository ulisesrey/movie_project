import glob
from movie_project.src.decompress_read import *
from movie_project.src.processing import calculate_days_on_air
from movie_project.src.processing import create_show_poster_dict
from movie_project.src.filtering import filter_by_language
from movie_project.src.filtering import filter_by_string_in_overview
from movie_project.src.filtering import filter_by_starting_year
from movie_project.src.filtering import filter_by_status
from movie_project.src.filtering import filter_genres
from movie_project.src.plotting import plot_count_per_year
from movie_project.src.plotting import plot_type_per_decade
from movie_project.src.plotting import genre_piechart


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

    # Show the top shows with the most days on air
    top_shows = 10
    days_on_air.sort_values(by="days_on_air", ascending=False).head(top_shows)

    ## Exercise 2.2:
    # Create a dictionary with show names and poster paths
    poster_dict = create_show_poster_dict(merged_df)

    # Show the first entries in the dictionary
    entries_to_show = 5
    for key, value in list(poster_dict.items())[:entries_to_show]:
        print(f"{key}: {value}")



    # Exercise 3:
    ## Exercise 3.1:
    language = "en"
    lang_df = filter_by_language(merged_df, language=language)

    strings_to_filter = ["crime", "mistery"]
    topic_lang_df = filter_by_string_in_overview(lang_df, strings_to_filter) # Not case sensitive
    
    # print it
    print(topic_lang_df["name"])

    # If you want to save the filtered dataframe
    topic_lang_df["overview"].to_csv("movie_project/reports/data/filtered.csv")

    ## Exercise 3.2:
    year = 2023
    status = "Canceled"
    entries_to_show = 20

    year_df = filter_by_starting_year(merged_df, start_year=year)
    status_year_df = filter_by_status(year_df, status=status)
    status_year_df[["name", "first_air_date", "status"]].head(entries_to_show)
    
    ## Exercise 3.3:
    language = "ja" # japanese
    entries_to_show = 20
    new_lang_df = filter_by_language(merged_df, language=language, strict=False)
    new_lang_df[["name", "original_name", "networks", "production_companies"]].head(entries_to_show)
    

    # Visualization part
    ## Exercise 4.1:
    plot_count_per_year(merged_df)


    ## Exercise 4.2:
    plot_type_per_decade(merged_df, start_decade=1940)

    ## Exercise 4.3:
    genres_df = filter_genres(merged_df, minimum_percentage=0.01)
    genre_piechart(merged_df)


    print("THE END")

