import unittest
from participant_info import ParticipantInfo
import sys
import io


def stub_stdout(testcase_inst):
    stderr = sys.stderr
    stdout = sys.stdout

    def cleanup():
        sys.stderr = stderr
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stderr = io.StringIO()
    sys.stdout = io.StringIO()


class TestParticipantInfo(unittest.TestCase):
    def test_create_correct_custom(self):
        custom = ParticipantInfo(0, 1596757823, "0000000012312123", 8)
        self.assertEqual(custom.getId(), 0)
        self.assertEqual(custom.getApplicationDate(), 1596757823)
        self.assertEqual(custom.getApplicationBeiJingDate(),
                         '2020-08-07 07:50:23')
        self.assertEqual(custom.getApplicationCode(), '0000000012312123')
        self.assertEqual(custom.getParticipantCount(), 0)
        self.assertEqual(custom.getRate(), 8)

    def test_create_failure_custom(self):
        custom = ParticipantInfo(0, 1596757823, "0000000012312123", 8)
        self.assertNotEqual(custom.getId(), 1)
        self.assertNotEqual(custom.getApplicationDate(), 159675782)
        self.assertNotEqual(custom.getApplicationBeiJingDate(),
                            '2020-08-07 07:51:23')
        self.assertNotEqual(custom.getApplicationCode(), '000000012312123')
        self.assertNotEqual(custom.getParticipantCount(), 1)
        self.assertNotEqual(custom.getRate(), 7)

    def test_correct_lottery_base_id(self):
        stub_stdout(self)
        custom = ParticipantInfo(0, 1596757823, "0000000012312123", 1)
        custom.appendLotteryBaseId(123)
        custom.appendLotteryBaseId(123)
        self.assertEqual(str(sys.stdout.getvalue()),
                         'lottery base id is enough\n')
        self.assertEqual(custom.getLotteryBaseId(), (123,))

    def test_failure_lottery_base_id(self):
        stub_stdout(self)
        custom = ParticipantInfo(0, 1596757823, "0000000012312123", 1)
        custom.appendLotteryBaseId(123)
        self.assertNotEqual(str(sys.stdout.getvalue()),
                            'lottery base id is enough\n')
        custom.appendLotteryBaseId(124)
        self.assertEqual(str(sys.stdout.getvalue()),
                         'lottery base id is enough\n')
        self.assertEqual(custom.getLotteryBaseId(), (123,))
        self.assertNotEqual(custom.getLotteryBaseId(), (123, 124))

        stub_stdout(self)
        custom = ParticipantInfo(0, 1596757823, "0000000012312123", 3)
        custom.appendLotteryBaseId(123)
        custom.appendLotteryBaseId(124)
        custom.appendLotteryBaseId(124)
        self.assertEqual(str(sys.stdout.getvalue()),
                         '124 is exist, ignore this id\n')
        custom.appendLotteryBaseId(125)
        custom.appendLotteryBaseId(125)
        self.assertEqual(custom.getLotteryBaseId(), (123, 124, 125))
        custom.appendLotteryBaseId(126)
        self.assertEqual(custom.getLotteryBaseId(), (123, 124, 125))
        self.assertNotEqual(custom.getLotteryBaseId(), (123, 124, 125, 126))
