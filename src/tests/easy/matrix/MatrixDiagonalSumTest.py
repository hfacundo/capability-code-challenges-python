import unittest
from src.components.easy.matrix.MatrixDiagonalSum import diagonal_sum


class MatrixDiagonalSumTest(unittest.TestCase):
    def test_DiagonalSum(self):
        test1 = diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(test1, 25)

        test2 = diagonal_sum([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
        self.assertEqual(test2, 8)

        test3 = diagonal_sum([[], [5]])
        self.assertEqual(test3, 5)


if __name__ == '__main__':
    unittest.main()
