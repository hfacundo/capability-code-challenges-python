import unittest
from src.components.easy.binarysearch.KthMissingNumber import find_kth_positive


class KthMissingNumberTest(unittest.TestCase):
    def test_FindKthPositive(self):
        test1 = find_kth_positive([2,3,4,7,11], 5)
        test2 = find_kth_positive([1,2,3,4], 2)

        self.assertEqual(test1, 9)
        self.assertEqual(test2, 6)


if __name__ == '__main__':
    unittest.main()
