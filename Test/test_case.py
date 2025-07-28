import unittest
import pandas as pd
from Test.data_validation import top_stadium

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



class stadium_count(unittest.TestCase):
    def test_returns_stadium_count(self):
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

        ])

        # Call the function
        result = stadium_count(data)

        # Reset index for comparison (optional)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))


if __name__ == '__main__':
    unittest.main()