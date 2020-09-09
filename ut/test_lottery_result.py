import unittest
from lottery_result import printLotteryResult
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
    def test_printLotteryResult(self):
        stub_stdout(self)
