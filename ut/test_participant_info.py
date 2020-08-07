import unittest
from participant_info import ParticipantInfo


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
