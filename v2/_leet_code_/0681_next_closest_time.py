import itertools


class Solution(object):
    def nextClosestTime(self, time):
        ans = start = 60 * int(time[:2]) + int(time[3:])
        elapsed = 24 * 60
        for h1, h2, m1, m2 in itertools.product(
            {int(x) for x in time if x != ":"}, repeat=4
        ):
            hours, mins = 10 * h1 + h2, 10 * m1 + m2
            if hours < 24 and mins < 60:
                cur = hours * 60 + mins
                if cur < start:
                    cur_elapsed = cur + 24 * 60 - start
                else:
                    cur_elapsed = cur - start
                if 0 < cur_elapsed < elapsed:
                    ans = cur
                    elapsed = cur_elapsed

        return "{:02d}:{:02d}".format(*divmod(ans, 60))


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual("19:39", s.nextClosestTime("19:34"))
        self.assertEqual("22:22", s.nextClosestTime("23:59"))


if __name__ == "__main__":
    unittest.main(exit=False)
