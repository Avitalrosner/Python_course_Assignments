#Testing that the processing works:

import unittest
import pandas as pd
from process_umi import load_data, calculate_log10

class TestProcessUmi(unittest.TestCase):

    def setUp(self):
        self.file_path = 'C:....../test_umi.csv'
        self.data = load_data(self.file_path)

    def test_load_data(self):
        self.assertEqual(len(self.data), 3)
        self.assertEqual(list(self.data.columns), ['patient', 'cancer', 'sum_of_umis'])

    def test_calculate_log10(self):
        expected_log10_values = pd.Series([4, 3, 2], name='log10_sum_of_umis')
        self.data = calculate_log10(self.data, 'sum_of_umis')
        calculated_log10_values = self.data['log10_sum_of_umis']
        pd.testing.assert_series_equal(calculated_log10_values, expected_log10_values)

if __name__ == "__main__":
    unittest.main()

