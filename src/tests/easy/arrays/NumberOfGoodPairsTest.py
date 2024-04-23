import unittest
from src.components.easy.arrays.NumberOfGoodPairs import num_identical_pairs


class NumberOfGoodPairsTest(unittest.TestCase):
    def test_NumberOfGoodPairs(self):
        self.assertEqual(num_identical_pairs([1,2,3,1,1,3]), 4)
        self.assertEqual(num_identical_pairs([1,1,1,1]), 6)
        self.assertEqual(num_identical_pairs([1,2,3]), 0)


if __name__ == '__main__':
    unittest.main()
