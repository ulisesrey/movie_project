import unittest
import glob
from movie_project.src.decompress_read import read_and_merge_csv


class DecompressAndRead(unittest.TestCase):
    
    def test_merged_df_length(self):
        csv_list = glob.glob("movie_project/data/*.csv")
        print("list of csv is:", csv_list)
        self.assertTrue(len(read_and_merge_csv(csv_list, id="id"))==486414)


unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)