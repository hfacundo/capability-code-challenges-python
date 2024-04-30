import unittest
from src.components.easy.dynamic.PascalTriangle import generate


class PascalTriangleTest(unittest.TestCase):
    def test_Generate(self):
        test1 = generate(5)
        expected1 = [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
        self.assertEqual(test1, expected1)

        test2 = generate(1)
        expected2 = [(1)]
        self.assertEqual(test2, expected2)


if __name__ == '__main__':
    unittest.main()
