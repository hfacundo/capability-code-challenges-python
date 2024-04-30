import unittest
from src.components.easy.twopointer.ShortestDistanceToChar import shortest_to_char


class ShortestDistanceToCharTest(unittest.TestCase):
    def test_ShortestToChar(self):
        test1 = shortest_to_char("loveleetcode", 'e')
        expected1 = [3,2,1,0,1,0,0,1,2,2,1,0]
        self.assertTrue(test1, expected1)

        test2 = shortest_to_char("aaab", 'b')
        expected2 = [3,2,1,0]
        self.assertTrue(test2, expected2)


if __name__ == '__main__':
    unittest.main()
