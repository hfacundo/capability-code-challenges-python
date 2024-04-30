import unittest
from src.components.easy.matrix.FlippingImage import flip_and_invert_image


def are_matrices_equal(test, expected):
    if len(test) != len(expected):
        return False

    for i in range(len(test)):
        if len(test[i]) != len(expected[i]):
            return False

    for i in range(len(test)):
        for j in range(len(test[i])):
            if test[i][j] != expected[i][j]:
                return False

    return True


class FlippingImageTest(unittest.TestCase):
    def test_FlipAndInvertImage(self):
        test1 = flip_and_invert_image([[1, 1, 0], [1, 0, 1], [0, 0, 0]])
        expected1 = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
        self.assertTrue(are_matrices_equal(test1, expected1))

        test2 = flip_and_invert_image([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]])
        expected2 = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
        self.assertTrue(are_matrices_equal(test2, expected2))


if __name__ == '__main__':
    unittest.main()
