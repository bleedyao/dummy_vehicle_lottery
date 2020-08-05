import unittest
from vehical_lottery import RandomInformation


class TestSeed(unittest.TestCase):
    def test_seed_equal(self):
        ri1 = RandomInformation(seed=100)
        ri2 = RandomInformation(seed=100)
        for i in range(500):
            result1 = ri1.randomApplicationCode()
            result2 = ri2.randomApplicationCode()
            self.assertEqual(result1, result2)

    def test_seed_not_equal(self):
        ri1 = RandomInformation(seed=100)
        ri2 = RandomInformation(seed=101)
        for i in range(500):
            result1 = ri1.randomApplicationCode()
            result2 = ri2.randomApplicationCode()
            self.assertNotEqual(result1, result2)

