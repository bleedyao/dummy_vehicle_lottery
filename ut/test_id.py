import unittest
from vehical_lottery import RandomInformation


class TestId(unittest.TestCase):
    def test_id_success(self):
        ri = RandomInformation()
        ids = ri.idGenerater()
        for i in range(20):
            next(ids)
        self.assertEqual(next(ids), 21)
        for i in range(20):
            next(ids)
        self.assertEqual(next(ids), 42)
    
    def test_id_failure(self):
        ri = RandomInformation()
        ids = ri.idGenerater()
        for i in range(20):
            next(ids)
        self.assertNotEqual(next(ids), 1)

