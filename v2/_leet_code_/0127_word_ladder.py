from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        index = defaultdict(set)
        for i in range(len(wordList[0])):
            for word in wordList:
                index[i].add(word[i])
        wordList = set(wordList)

        frontier = deque([(1, beginWord)])
        visited = set([beginWord])

        while len(frontier) > 0:
            cost, cur_word = frontier.popleft()

            if cur_word == endWord:
                return cost

            for i in range(len(cur_word)):
                for c in index[i]:
                    candidate = cur_word[:i] + c + cur_word[i + 1 :]
                    if candidate in wordList and candidate not in visited:
                        visited.add(candidate)
                        frontier.append((cost + 1, candidate))

        return 0


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertEqual(
            5, s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
        )

        self.assertEqual(
            0, s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
        )


if __name__ == "__main__":
    unittest.main()
