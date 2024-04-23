import unittest
from src.components.easy.arrays.FirstPalindrome import find_first_palindrome


class FindFirstPalindromeTest(unittest.TestCase):
    def test_FindFirstPalindrome(self):
        test1 = find_first_palindrome(["abc","car","ada","racecar","cool"])
        test2 = find_first_palindrome(["notapalindrome","racecar"])
        test3 = find_first_palindrome(["def","ghi"])

        self.assertEqual(test1, "ada")
        self.assertEqual(test2, "racecar")
        self.assertEqual(test3, "")


if __name__ == '__main__':
    unittest.main()
