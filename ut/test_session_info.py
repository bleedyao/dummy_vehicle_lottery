
import unittest
from vehical_lottery import SessionInfo


class TestSessionInfo(unittest.TestCase):
    def test_success_object(self):
        session = SessionInfo(1, '第一期摇号结果', 100, 2)
        self.assertEqual(session.getId(), 1)
        self.assertEqual(session.getDescript(), '第一期摇号结果')
        self.assertEqual(session.getValidApplictionCodeCount(), 100)
        self.assertEqual(session.getTotalWins(), 2)
        session.setStartTime(1000)
        session.setEndTime(1001)
        self.assertEqual(session.getDuration(), 1)
        for i in range(400_000):
            session = SessionInfo()
            self.assertGreaterEqual(session.getSeed(), 0)
            self.assertLess(session.getSeed(), 1_000_000)

    def test_failure_object(self):
        session = SessionInfo(1, '第一期摇号结果', 100, 2)
        session.setStartTime(-1)
        self.assertEqual(session.getStartTime(), 0)
        session.setStartTime('123')
        self.assertEqual(session.getStartTime(), 0)
        session.setStartTime(2000)
        session.setEndTime(-1)
        self.assertEqual(session.getEndTime(), 2000)
        session.setEndTime('')
        self.assertEqual(session.getEndTime(), 2000)
        session.setEndTime(1000)
        self.assertEqual(session.getEndTime(), 2000)
