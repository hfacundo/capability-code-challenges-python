import unittest
from src.components.easy.strings.JewelsAndStones import num_jewels_in_stones


class JewelsAndStonesTest(unittest.TestCase):
    def test_numJewelsInsStone(self):
        self.assertEqual(num_jewels_in_stones("aA", "aAAbbbb"), 3)
        self.assertEqual(num_jewels_in_stones("z", "ZZ"), 0)


if __name__ == '__main__':
    unittest.main()
