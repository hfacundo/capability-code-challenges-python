import unittest
from src.components.easy.strings.BalancedString import balanced_string_split


class BalancedStringTest(unittest.TestCase):
    def test_BalancedStringSplit(self):
        self.assertEqual(balanced_string_split("RLRRLLRLRL"), 4)
        self.assertEqual(balanced_string_split("RLRRRLLRLL"), 2)
        self.assertEqual(balanced_string_split("LLLLRRRR"), 1)


if __name__ == '__main__':
    unittest.main()
