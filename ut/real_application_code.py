import unittest
from vehical_lottery import RandomInformation


class RealApplicationCode(unittest.TestCase):
    def test_real_application_code(self):
        tempStr = ''
        tempMap = dict()
        ri = RandomInformation()
        for i in range(ri.getMaxNumber()):
            tempStr = ri.randomApplicationCode()
            self.assertTrue(tempStr not in tempMap)
            tempMap[tempStr] = 1
        else:
            with self.assertRaises(Exception):
                ri.randomApplicationCode()
