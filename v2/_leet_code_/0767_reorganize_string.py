from heapq import heappop, heappush
from collections import Counter


class Solution:
    def reorganizeString(self, S: "str") -> "str":
        hit_map = Counter(S)
        kLoopSize = 2

        heap = []
        for k, v in hit_map.items():
            heappush(heap, (-v, k))

        ans = []
        while heap:
            if len(heap) == 1 and heap[0][0] < -1:
                return ""

            next_round = []
            for _ in range(kLoopSize):
                if not heap:
                    break

                neg_count, letter = heappop(heap)
                ans.append(letter)
                if neg_count < -1:
                    next_round.append((neg_count + 1, letter))

            for p, l in next_round:
                heappush(heap, (p, l))

        return "".join(ans)


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual("vlvov", s.reorganizeString("vvvlo"))
        self.assertEqual("aba", s.reorganizeString("aab"))
        self.assertEqual("", s.reorganizeString("aaab"))
        self.assertEqual("abab", s.reorganizeString("baab"))
        self.assertEqual("ababc", s.reorganizeString("baabc"))
        self.assertEqual("", s.reorganizeString(""))


if __name__ == "__main__":
    unittest.main()
