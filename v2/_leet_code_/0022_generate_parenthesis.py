class Solution(object):
    def generateParenthesis(self, n):
        return [r for r in self._generateParenthesis(n)]


    def _generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        if n == 1:
            return ["()"]

        result = set()
        for sub_result in self.generateParenthesis(n - 1):
            for i in range(len(sub_result)):
                result.add(sub_result[:i] + "()" + sub_result[i:])

        return result


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        print(s.generateParenthesis(3))


if __name__ == "__main__":
    unittest.main()
