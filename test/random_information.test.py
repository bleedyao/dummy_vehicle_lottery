import unittest
from vehical_lottery import RandomInformation


class TestRandomInfo(unittest.TestCase):
    def test_applicatoin_code(self):
        ri = RandomInformation()
        test1 = ri.randomApplicationCode()
        test2 = ri.randomApplicationCode()
        self.assertNotEqual(test1, test2)


if __name__ == "__main__":
    unittest.main()
