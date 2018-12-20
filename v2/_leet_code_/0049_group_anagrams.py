class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for s in strs:
            k = self._key(s)
            if k not in groups:
                groups[k] = []
            groups[k].append(s)

        return [v for k, v in groups.items()]

    def _key(self, word):
        return "".join(sorted(word))


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']],
            s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
        )

        self.assertEqual(
            [['eat'], ['tan'], ['bat']],
            s.groupAnagrams(["eat", "tan", "bat"]),
        )

        self.assertEqual(
            [['eat']],
            s.groupAnagrams(["eat"]),
        )

        self.assertEqual(
            [],
            s.groupAnagrams([]),
        )


if __name__ == "__main__":
    unittest.main()
