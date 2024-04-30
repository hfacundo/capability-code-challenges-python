import unittest
from src.components.easy.recursion.FibonacciNumber import fib


class FibonacciNumberTest(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)


if __name__ == '__main__':
    unittest.main()
