import unittest
from src.components.easy.strings.DefangingIpAddress import defang_ip_address


class DefangingIpAddressTest(unittest.TestCase):
    def test_DefangIpAddress(self):
        self.assertEqual(defang_ip_address("1.1.1.1"), "1[.]1[.]1[.]1")
        self.assertEqual(defang_ip_address("255.100.50.0"), "255[.]100[.]50[.]0")


if __name__ == '__main__':
    unittest.main()
