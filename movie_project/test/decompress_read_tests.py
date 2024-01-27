import unittest
import glob
from movie_project.src.decompress_read import read_and_merge_csv


class DecompressAndRead(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Finding csv files")
        cls._csv_list = glob.glob("movie_project/data/*.csv")
        print("list of csv is:", cls._csv_list)

    def test_merged_df_length(self):
        self.assertTrue(len(read_and_merge_csv(self._csv_list, id="id"))==486414)


unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)