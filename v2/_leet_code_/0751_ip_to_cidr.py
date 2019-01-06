from math import log


class Solution:
    def intToIp(self, n):
        parts = []
        for i in [24, 16, 8, 0]:
            parts.append((n >> i) & 255)
        return ".".join([str(p) for p in parts])

    def ipToInt(self, ip):
        res = 0
        for part in ip.split("."):
            res *= 256
            res += int(part)
        return res

    def indexLowestSetBit(self, n):
        return int(log(n & (-n), 2))

    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        ans = []
        start = self.ipToInt(ip)
        while n > 0:
            idx = min(self.indexLowestSetBit(start), int(log(n, 2)))
            ans.append("{}/{}".format(self.intToIp(start), 32 - idx))
            
            n -= 2 ** idx
            start += 2 ** idx
        return ans


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual("255.0.0.7", s.intToIp(s.ipToInt("255.0.0.7")))
        self.assertEqual(
            ["255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"],
            s.ipToCIDR("255.0.0.7", 10),
        )


if __name__ == "__main__":
    unittest.main()
