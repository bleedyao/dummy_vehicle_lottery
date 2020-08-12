import unittest
from time_util import timeFormat
from time_util import hmsTransfor
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


class TestTimeUtil(unittest.TestCase):
    def test_success_time_format(self):
        timeStr = timeFormat(1597021182)
        self.assertEqual(timeStr, '2020-08-10 08:59:42')

    def test_failure_time_format(self):
        stub_stdout(self)
        timeStr = timeFormat('1597021182')
        self.assertEqual(str(sys.stdout.getvalue()),
                         '1597021182 is not type of int\n')
        self.assertEqual(timeStr, '1597021182')

        stub_stdout(self)
        timeStr = timeFormat(-10)
        self.assertNotEqual(timeStr, '')

    def test_success_hmsTransfor(self):
        resultTime = hmsTransfor(60)
        self.assertEqual(resultTime, '00小时:01分:00秒')
        resultTime = hmsTransfor(3600)
        self.assertEqual(resultTime, '01小时:00分:00秒')

    def test_failure_hmsTransfor(self):
        stub_stdout(self)
        resultTime = hmsTransfor('3600')
        self.assertEqual(str(sys.stdout.getvalue()),
                         '3600 is not type of int\n')
        stub_stdout(self)
        resultTime = hmsTransfor(-1)
        self.assertEqual(str(sys.stdout.getvalue()),
                         '-1 must be positive\n')
