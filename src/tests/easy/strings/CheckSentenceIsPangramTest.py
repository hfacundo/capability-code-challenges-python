import unittest
from src.components.easy.strings.CheckSentenceIsPangram import check_if_pangram


class CheckSentenceIsPangramTest(unittest.TestCase):
    def test_CheckIfPangram(self):
        self.assertTrue(check_if_pangram("thequickbrownfoxjumpsoverthelazydog"))
        self.assertFalse(check_if_pangram("leetcode"))


if __name__ == '__main__':
    unittest.main()
