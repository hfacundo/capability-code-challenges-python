import unittest
from src.components.easy.math.MissingNumber import missing_number


class MissingNumberTest(unittest.TestCase):
    def test_MissingNumber(self):
        self.assertEqual(missing_number([3,0,1]), 2)
        self.assertEqual(missing_number([0,1]), 2)
        self.assertEqual(missing_number([9,6,4,2,3,5,7,0,1]), 8)


if __name__ == '__main__':
    unittest.main()
