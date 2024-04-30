import unittest
from src.components.easy.strings.FirstUniqueChar import first_unique_char


class FirstUniqueCharTest(unittest.TestCase):
    def test_FirstUniqueChar(self):
        self.assertEqual(first_unique_char("leetcode"), 0)
        self.assertEqual(first_unique_char("loveleetcode"), 2)
        self.assertEqual(first_unique_char("aabb"), -1)


if __name__ == '__main__':
    unittest.main()
