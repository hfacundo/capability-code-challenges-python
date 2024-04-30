import unittest
from src.components.easy.math.RomanToInteger import roman_to_int


class RomanToIntegerTest(unittest.TestCase):
    def test_RomanToInt(self):
        self.assertEqual(roman_to_int("III"), 3)
        self.assertEqual(roman_to_int("LVIII"), 58)
        self.assertEqual(roman_to_int("MCMXCIV"), 1994)


if __name__ == '__main__':
    unittest.main()
