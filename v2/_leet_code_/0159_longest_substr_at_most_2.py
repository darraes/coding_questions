class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        def extrat_smaller(window):
            min_k, min_v = None, None
            for k, v in window.items():
                if min_k is None or min_v > v:
                    min_k, min_v = k, v

            del window[min_k]
            return min_v

        window = {}
        begin = end = max_length = 0
        for i in range(len(s)):
            end = i
            window[s[i]] = i
            if len(window) == 3:
                begin = extrat_smaller(window) + 1
            max_length = max(max_length, end - begin + 1)

        return max_length


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(3, s.lengthOfLongestSubstringTwoDistinct("eceba"))
        self.assertEqual(5, s.lengthOfLongestSubstringTwoDistinct("ccaabbb"))
        self.assertEqual(5, s.lengthOfLongestSubstringTwoDistinct("ccaabbbd"))
        self.assertEqual(1, s.lengthOfLongestSubstringTwoDistinct("c"))
        self.assertEqual(3, s.lengthOfLongestSubstringTwoDistinct("ccc"))
        self.assertEqual(5, s.lengthOfLongestSubstringTwoDistinct("cccbb"))


if __name__ == "__main__":
    unittest.main(exit=False)
