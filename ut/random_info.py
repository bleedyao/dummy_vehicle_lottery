import unittest
from vehical_lottery import RandomInformation


class TestRandomApplicationCode(unittest.TestCase):

    def test_application_code_nagative_number(self):
        ri = RandomInformation(-1)
        with self.assertRaises(Exception):
            ri.randomApplicationCode()
        ri = RandomInformation(-10)
        with self.assertRaises(Exception):
            ri.randomApplicationCode()

    def test_application_code_zero(self):
        ri = RandomInformation(0)
        with self.assertRaises(Exception):
            ri.randomApplicationCode()

    def test_application_code_one(self):
        ri = RandomInformation(1)
        ri.randomApplicationCode()
        with self.assertRaises(Exception):
            ri.randomApplicationCode()

    def test_application_code_five(self):
        n = 5
        tempList = []
        temp = ''
        ri = RandomInformation(n)
        for i in range(n):
            temp = ri.randomApplicationCode()
            self.assertTrue(temp not in tempList)
            tempList.append(temp)
        else:
            with self.assertRaises(Exception):
                ri.randomApplicationCode()

    def test_application_code_ten(self):
        n = 10
        tempList = []
        temp = ''
        ri = RandomInformation(n)
        for i in range(n):
            temp = ri.randomApplicationCode()
            self.assertTrue(temp not in tempList)
            tempList.append(temp)
        else:
            with self.assertRaises(Exception):
                ri.randomApplicationCode()

    def test_application_code_hundred(self):
        n = 100
        tempList = []
        temp = ''
        ri = RandomInformation(n)
        for i in range(n):
            temp = ri.randomApplicationCode()
            self.assertTrue(temp not in tempList)
            tempList.append(temp)
        else:
            with self.assertRaises(Exception):
                ri.randomApplicationCode()

    def test_application_code_five_hundred(self):
        n = 500
        tempList = []
        temp = ''
        ri = RandomInformation(n)
        for i in range(n):
            temp = ri.randomApplicationCode()
            self.assertTrue(temp not in tempList)
            tempList.append(temp)
        else:
            with self.assertRaises(Exception):
                ri.randomApplicationCode()

    def test_application_code_two_thousand(self):
        n = 2000
        tempList = []
        temp = ''
        ri = RandomInformation(n)
        for i in range(n):
            temp = ri.randomApplicationCode()
            self.assertTrue(temp not in tempList)
            tempList.append(temp)
        else:
            with self.assertRaises(Exception):
                ri.randomApplicationCode()

    def test_application_code_ten_thousand(self):
        n = 10000
        tempList = []
        temp = ''
        ri = RandomInformation(n)
        for i in range(n):
            temp = ri.randomApplicationCode()
            self.assertTrue(temp not in tempList)
            tempList.append(temp)
        else:
            with self.assertRaises(Exception):
                ri.randomApplicationCode()
    def test_application_code_fifty_thousand(self):
        n = 50000
        tempList = []
        temp = ''
        ri = RandomInformation(n)
        for i in range(n):
            temp = ri.randomApplicationCode()
            self.assertTrue(temp not in tempList)
            tempList.append(temp)
        else:
            with self.assertRaises(Exception):
                ri.randomApplicationCode()

    def test_application_code_hundred_thousand(self):
        n = 100000
        tempList = []
        temp = ''
        ri = RandomInformation(n)
        for i in range(n // 2):
            temp = ri.randomApplicationCode()
            self.assertTrue(temp not in tempList)
            tempList.append(temp)



if __name__ == '__main__':
    unittest.main()
