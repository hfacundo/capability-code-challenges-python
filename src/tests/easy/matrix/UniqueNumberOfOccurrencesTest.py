import unittest
from src.components.easy.matrix.UniqueNumberOfOccurrences import unique_occurrences


class UniqueNumberOfOccurrencesTest(unittest.TestCase):
    def test_UniqueOccurrences(self):
        self.assertTrue(unique_occurrences([1, 2, 2, 1, 1, 3]))
        self.assertFalse(unique_occurrences([1, 2]))
        self.assertTrue(unique_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))


if __name__ == '__main__':
    unittest.main()
