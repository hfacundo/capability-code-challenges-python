import unittest
from src.components.easy.lists.FindWordsContaningCharacter import find_words_containing


class FindWordsContainingCharacterTest(unittest.TestCase):
    def test_findWordsContaining(self):
        test1 = find_words_containing(["leet", "code"], 'e')
        test2 = find_words_containing(["abc", "bcd", "aaaa", "cbc"], 'a')
        test3 = find_words_containing(["abc", "bcd", "aaaa", "cbc"], 'z')

        self.assertIsNotNone(test1)
        self.assertEqual(test1[0], 0)
        self.assertEqual(test1[1], 1)

        self.assertIsNotNone(test2)
        self.assertEqual(test2[0], 0)
        self.assertEqual(test2[1], 2)

        self.assertIsNone(test3)


if __name__ == '__main__':
    unittest.main()
