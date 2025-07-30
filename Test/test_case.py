import unittest
import pandas as pd
from Test.data_validation import *

class TestTopStadium(unittest.TestCase):
    def test_top_stadium_returns_top_5(self):
        # Sample input data
        data = [
            {'rank': 1, 'stadium': 'Michigan Stadium', 'capacity': 90000},
            {'rank': 2, 'stadium': 'Wembley Stadium', 'capacity': 80000},
            {'rank': 3, 'stadium': 'stadio Azteca', 'capacity': 75000},
            {'rank': 4, 'stadium': 'Croke Park', 'capacity': 70000},
            {'rank': 5, 'stadium': 'Shah Alam Stadium', 'capacity': 85000},
            {'rank': 6, 'stadium': 'Empower Field', 'capacity': 60000},
        ]

        # Expected output DataFrame
        expected = pd.DataFrame([
            {'rank': 1, 'stadium': 'Michigan Stadium', 'capacity': 90000},
            {'rank': 5, 'stadium': 'hah Alam Stadium', 'capacity': 85000},
            {'rank': 2, 'stadium': 'SWembley Stadium', 'capacity': 80000},
            {'rank': 3, 'stadium': 'stadio Azteca', 'capacity': 75000},
            {'rank': 4, 'stadium': 'Croke Park', 'capacity': 70000},
        ])

        # Call the function
        result = top_stadium(data)

        # Reset index for comparison (optional)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))



class stadiumCount(unittest.TestCase):
    def test_returns_stadium_count(self):
        # Sample input data
        data = [
            {'rank': 1, 'stadium': 'Michigan Stadium', 'capacity': 90000, 'country': 'USA'},
            {'rank': 2, 'stadium': 'Wembley Stadium', 'capacity': 80000, 'country': 'UK'},
            {'rank': 3, 'stadium': 'Stadio Azteca', 'capacity': 75000, 'country': 'Mexico'},
            {'rank': 4, 'stadium': 'Croke Park', 'capacity': 70000, 'country': 'Ireland'},
            {'rank': 5, 'stadium': 'Shah Alam Stadium', 'capacity': 85000, 'country': 'Malaysia'},
            {'rank': 6, 'stadium': 'Empower Field', 'capacity': 60000, 'country': 'USA'},
        ]

        # Expected output DataFrame
        expected = pd.DataFrame([
            {'stadium_count': 2, 'country': 'USA'},
            {'stadium_count': 1, 'country': 'UK'},
            {'stadium_count': 1, 'country': 'Mexico'},
            {'stadium_count': 1, 'country': 'Ireland'},
            {'stadium_count': 1, 'country': 'Malaysia'}
        ])

        # Call the function
        result = stadium_count(data)

        # Reset index for comparison (optional)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))




class stadiumCapacity(unittest.TestCase):
    def test_returns_stadium_capacity(self):
        # Sample input data
        data = [
            {'rank': 1, 'stadium': 'Michigan Stadium', 'capacity': 90000, 'country': 'USA', 'region': 'North America'},
            {'rank': 2, 'stadium': 'Wembley Stadium', 'capacity': 80000, 'country': 'UK', 'region': 'Europe'},
            {'rank': 3, 'stadium': 'Stadio Azteca', 'capacity': 75000, 'country': 'Mexico', 'region': 'North America'},
            {'rank': 4, 'stadium': 'Croke Park', 'capacity': 70000, 'country': 'Ireland', 'region': 'Europe'},
            {'rank': 5, 'stadium': 'Shah Alam Stadium', 'capacity': 85000, 'country': 'Malaysia', 'region': 'East Asia'},
            {'rank': 6, 'stadium': 'Empower Field', 'capacity': 60000, 'country': 'USA', 'region': 'North America'}
        ]

        # Expected output DataFrame
        expected = pd.DataFrame([
            {'region': 'East Asia', 'avg_capacity': 85000.0},
            {'region': 'North America', 'avg_capacity': 75000.0},
            {'region': 'Europe', 'avg_capacity': 75000.0}
        ])

        # Call the function
        result = stadium_capacity(data)

        # Reset index for comparison (optional)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))



class stadiumRank(unittest.TestCase):
    def test_returns_stadium_rank(self):
        # Sample input data
        data = [
            {'rank': 1, 'stadium': 'Michigan Stadium', 'capacity': 90000, 'country': 'USA', 'region': 'North America'},
            {'rank': 2, 'stadium': 'Wembley Stadium', 'capacity': 80000, 'country': 'UK', 'region': 'Europe'},
            {'rank': 3, 'stadium': 'Stadio Azteca', 'capacity': 75000, 'country': 'Mexico', 'region': 'North America'},
            {'rank': 4, 'stadium': 'Croke Park', 'capacity': 70000, 'country': 'Ireland', 'region': 'Europe'},
            {'rank': 5, 'stadium': 'Shah Alam Stadium', 'capacity': 85000, 'country': 'Malaysia',
             'region': 'East Asia'},
            {'rank': 6, 'stadium': 'Empower Field', 'capacity': 60000, 'country': 'USA', 'region': 'North America'},
        ]
        expected = pd.DataFrame([
            {'rank': 1, 'stadium': 'Michigan Stadium', 'region': 'North America', 'region_rank': 1.0},
            {'rank': 2, 'stadium': 'Wembley Stadium', 'region': 'Europe', 'region_rank': 1.0},
            {'rank': 3, 'stadium': 'Stadio Azteca', 'region': 'North America', 'region_rank': 2.0},
            {'rank': 4, 'stadium': 'Croke Park', 'region': 'Europe', 'region_rank': 2.0},
            {'rank': 5, 'stadium': 'Shah Alam Stadium', 'region': 'East Asia', 'region_rank': 1.0},
            {'rank': 6, 'stadium': 'Empower Field', 'region': 'North America', 'region_rank': 3.0}
        ])

        # Call the function
        result = stadium_rank(data)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))



class stadiumCapacity(unittest.TestCase):
    def test_returns_stadium_rank(self):
        # Sample input data
        data = data = [
                {'rank': 1, 'stadium': 'Michigan Stadium', 'capacity': 90000, 'country': 'USA', 'region': 'North America'},
                {'rank': 2, 'stadium': 'Wembley Stadium', 'capacity': 80000, 'country': 'UK', 'region': 'Europe'},
                {'rank': 3, 'stadium': 'Stadio Azteca', 'capacity': 75000, 'country': 'Mexico', 'region': 'North America'},
                {'rank': 4, 'stadium': 'Croke Park', 'capacity': 70000, 'country': 'Ireland', 'region': 'Europe'},
                {'rank': 5, 'stadium': 'Shah Alam Stadium', 'capacity': 85000, 'country': 'Malaysia', 'region': 'East Asia'},
                {'rank': 6, 'stadium': 'Empower Field', 'capacity': 60000, 'country': 'USA', 'region': 'North America'},
            ]
        expected = pd.DataFrame([
                    {'rank': 1, 'stadium': 'Michigan Stadium', 'capacity': 90000, 'country': 'USA', 'region': 'North America', 'avg_capacity': 75000.0},
                    {'rank': 2, 'stadium': 'Wembley Stadium', 'capacity': 80000, 'country': 'UK', 'region': 'Europe', 'avg_capacity': 75000.0}
                    ])

        # Call the function
        result = stadium_capacity_avg(data)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))



if __name__ == '__main__':
    unittest.main()