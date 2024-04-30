import unittest
from src.components.easy.math.PalindromeNumber import is_palindrome


class PalindromeNumberTest(unittest.TestCase):
    def test_IsPalindrome(self):
        self.assertTrue(is_palindrome(121))
        self.assertFalse(-121)
        self.assertFalse(10)


if __name__ == '__main__':
    unittest.main()
