"""Module to perform tests"""
import unittest
import glob
from movie_project.src.decompress_read import read_and_merge_csv_files
from movie_project.src.decompress_read import read_and_merge_csv_to_dict


class Read(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
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
#add a test to check if there are nans in values of ordered dict
import unittest
import glob

#len(df[df['homepage'].isna()]["homepage"])==112181
#len(df[df['poster_path'].isna()]["poster_path"])==57631

#verify that date columns are datetime type


# class Filter(unittest.TestCase):


# class Plot(unittest.TestCase):

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)