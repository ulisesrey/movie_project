"""Main module to run the project."""
import argparse
import glob
from movie_project.src.decompress_read import decompress_file
from movie_project.src.decompress_read import read_and_merge_csv_files
from movie_project.src.decompress_read import read_and_merge_csv_to_dict
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

# Reading part
def read():
    """Read the dataset."""
    # get the list of csv files
    csv_list = glob.glob("movie_project/data/*.csv")

    # merge the csv files into a single dataframe
    df = read_and_merge_csv_files(csv_list, id="id")
    # optional to save the df
    #df.to_csv("movie_project/reports/data/merged_df.csv", index=False)

    # # merge the csv files into a single dictionary
    merged_dict = read_and_merge_csv_to_dict(csv_list, id="id")
    
    return df, merged_dict

# Processing part
def process(merged_df):
    """Process the dataset."""
    # Exercise 2:
    ## Exercise 2.1:
    days_on_air = calculate_days_on_air(merged_df)

    # Show the top shows with the most days on air
    TOP_SHOWS = 10
    print("These are the top shows with the most days on air:")
    days_on_air.sort_values(by="days_on_air", ascending=False).head(TOP_SHOWS)

    ## Exercise 2.2:
    # Create a dictionary with show names and poster paths
    poster_dict = create_show_poster_dict(merged_df)

    # Show the first entries in the dictionary
    ENTRIES_TO_SHOW = 5
    print("These are some entries with the links to the posters:")
    for key, value in list(poster_dict.items())[:ENTRIES_TO_SHOW]:
        print(f"{key}: {value}")

# Filtering part
def filters(merged_df):
    """Apply filters to the dataset."""
    # Exercise 3:
    ## Exercise 3.1:
    LANGUAGE = "en"
    lang_df = filter_by_language(merged_df, language=LANGUAGE)

    strings_to_filter = ["crime", "mistery"]
    topic_lang_df = filter_by_string_in_overview(lang_df, strings_to_filter)

    # print it
    print("\nThese are the movies in language \"{}\" with the topics {}:".format(LANGUAGE, strings_to_filter))
    print(topic_lang_df["name"].to_string(index=False))

    # If you want to save the filtered dataframe
    # topic_lang_df["overview"].to_csv("movie_project/reports/data/filtered.csv")

    ## Exercise 3.2:
    YEAR = 2023
    STATUS = "Canceled"
    ENTRIES_TO_SHOW = 20

    year_df = filter_by_starting_year(merged_df, start_year=YEAR)
    status_year_df = filter_by_status(year_df, status=STATUS)
    print(f"\nThese are the shows that started in {YEAR} and were {STATUS}:")
    print(status_year_df[["name", "first_air_date", "status"]].head(ENTRIES_TO_SHOW))

    ## Exercise 3.3:
    LANGUAGE = "ja" # japanese
    ENTRIES_TO_SHOW = 20
    new_lang_df = filter_by_language(merged_df, language=LANGUAGE, strict=False)
    print(f"\nThese are the some shows that are in \"{LANGUAGE}\":")
    print(new_lang_df[["name", "original_name", "networks", "production_companies"]].head(ENTRIES_TO_SHOW))

# Visualization part
def plot(merged_df):
    """Make all the plots."""
    ## Exercise 4.1:
    plot_count_per_year(merged_df)

    ## Exercise 4.2:
    plot_type_per_decade(merged_df, start_decade=1940, normalize=True)

    ## Exercise 4.3:
    genres_series = filter_genres(merged_df, minimum_percentage=0.01)
    genre_piechart(genres_series)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Movie project Script")
    parser.add_argument("--decompress", action="store_true", help="Decompress the compressed file")
    parser.add_argument("--process", action="store_true", help="Process the dataset")
    parser.add_argument("--filters", action="store_true", help="Apply request filters to the dataset")
    parser.add_argument("--plot", action="store_true", help="Generate the requested plots")
    parser.add_argument('--all', action='store_true', help='Run all blocks')

    args = parser.parse_args()

    if args.decompress or args.all:
        # Exercise 1:
        # decompress the compressed file
        decompress_file("movie_project/data/TMDB.zip", "movie_project/data/")

    # read always unless command was decompress
    if not args.decompress:
        # reading part
        merged_df, merged_dict = read()

    if args.all:
        process(merged_df)
        filters(merged_df)
        plot(merged_df)
        
    if args.process:
        # processing part
        process(merged_df)
    
    if args.filters:
        # filtering part
        filters(merged_df)
    
    if args.plot:
        # visualization part
        plot(merged_df) 

    print("\nTHE END")
