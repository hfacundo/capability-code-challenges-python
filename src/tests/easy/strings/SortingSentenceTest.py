import unittest
from src.components.easy.strings.SortingSentence import sorting_sentence


class SortingSentenceTest(unittest.TestCase):
    def test_SortingSentence(self):
        self.assertEqual(sorting_sentence("is2 sentence4 This1 a3"), "This is a sentence")
        self.assertEqual(sorting_sentence("Myself2 Me1 I4 and3"), "Me Myself and I")


if __name__ == '__main__':
    unittest.main()
