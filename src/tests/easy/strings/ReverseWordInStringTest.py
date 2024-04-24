import unittest
from src.components.easy.strings.ReverseWordInString import reverse_word


class ReverseWordInStringTest(unittest.TestCase):
    def test_ReverseWord(self):
        self.assertEqual(reverse_word("Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc")
        self.assertEqual(reverse_word("Mr Ding"), "rM gniD")


if __name__ == '__main__':
    unittest.main()
