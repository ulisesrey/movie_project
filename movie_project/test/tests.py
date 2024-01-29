"""Module to perform tests"""
import unittest
import glob
from movie_project.src.decompress_read import decompress_file
from movie_project.src.decompress_read import read_and_merge_csv_files
from movie_project.src.decompress_read import read_and_merge_csv_to_dict
from movie_project.src.processing import calculate_days_on_air
from movie_project.src.processing import create_show_poster_dict
from movie_project.src.filtering import filter_by_starting_year
from movie_project.src.filtering import filter_by_status
from movie_project.src.filtering import filter_genres
import pandas as pd


class Read(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        decompress_file("movie_project/data/TMDB.zip")
        print("Finding csv files")
        cls._csv_list = glob.glob("movie_project/data/*.csv")
        print("list of csv is:", cls._csv_list)

    def test_merged_df_length(self):
        self.assertTrue(len(read_and_merge_csv_files(self._csv_list, my_id="id"))==162138)


    def test_merged_df_columns(self):
        self.assertTrue(len(read_and_merge_csv_files(self._csv_list, my_id="id").columns)==29)
        self.assertIn("id", read_and_merge_csv_files(self._csv_list, my_id="id").columns)
        self.assertIn("name", read_and_merge_csv_files(self._csv_list, my_id="id").columns)


    def test_dict_type(self):
        self.assertIsInstance(read_and_merge_csv_to_dict(self._csv_list, my_id="id"), dict)
        

class Process(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        decompress_file("movie_project/data/TMDB.zip")
        print("Finding csv files")
        cls._csv_list = glob.glob("movie_project/data/*.csv")
        print("list of csv is:", cls._csv_list)
        cls._merged_df = read_and_merge_csv_files(cls._csv_list, my_id="id")
    
    def test_days_on_air(self):
        self.assertIn("days_on_air", calculate_days_on_air(self._merged_df).columns)
        self.assertIn("id", calculate_days_on_air(self._merged_df).columns)
        self.assertIn("name", calculate_days_on_air(self._merged_df).columns)
        self.assertTrue(calculate_days_on_air(self._merged_df)["days_on_air"].dtype=="timedelta64[ns]")

    def test_create_show_poster_dict(self):
        self.assertIsInstance(create_show_poster_dict(self._merged_df), dict)


class Filter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        decompress_file("movie_project/data/TMDB.zip")
        print("Finding csv files")
        cls._csv_list = glob.glob("movie_project/data/*.csv")
        print("list of csv is:", cls._csv_list)
        cls._merged_df = read_and_merge_csv_files(cls._csv_list, my_id="id")
        cls._starting_year = 2004
        cls._language = "en"
        cls._status = "Canceled"

    def test_filter_by_starting_year(self):
        self.assertIsInstance(filter_by_starting_year(self._merged_df, self._starting_year), pd.DataFrame)


    def test_filter_by_status(self):
        self.assertIsInstance(filter_by_status(self._merged_df, self._status), pd.DataFrame)


    def test_filter_genres(self):
        self.assertIsInstance(filter_genres(self._merged_df, 0.01), pd.Series)

# class Plot(unittest.TestCase): Does not have test units
        # because we dont want to generate plot during testing

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)