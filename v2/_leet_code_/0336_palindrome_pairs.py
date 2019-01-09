def is_palindrome(letters):
    s = 0
    e = len(letters) - 1

    while s < e:
        if letters[s] != letters[e]:
            return False
        s += 1
        e -= 1
    return True


class TrieNode:
    def __init__(self, is_end):
        self.edges = {}
        self.end_word_idxs = set([])
        self.words = []


class Trie:
    def __init__(self):
        self.root = TrieNode(is_end=False)

    def insert(self, term, word_idx):
        current = self.root

        idx = 0
        while idx < len(term):
            current.words.append((term, word_idx))
            if term[idx] not in current.edges:
                current.edges[term[idx]] = TrieNode(is_end=False)
            current = current.edges[term[idx]]
            idx += 1

        current.end_word_idxs.add(word_idx)
        current.words.append((term, word_idx))

    def search(self, term, my_idx):
        current = self.root
        answer = []

        idx = 0
        while idx < len(term):
            if current.end_word_idxs and is_palindrome(list(term[idx:])):
                for word_idx in current.end_word_idxs:
                    answer.append([my_idx, word_idx])

            if term[idx] not in current.edges:
                return answer
            current = current.edges[term[idx]]
            idx += 1

        for (letters, word_idx) in current.words:
            if word_idx != my_idx and is_palindrome(letters[idx:]):
                answer.append([my_idx, word_idx])
        return answer


class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ans = []
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(word[::-1], i)

        for i, word in enumerate(words):
            ans.extend(trie.search(word, i))

        return ans


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertEqual([[1, 0]], s.palindromePairs(["a", "abb"]))
        self.assertEqual([[0, 1]], s.palindromePairs(["a", "bba"]))

        self.assertEqual([[0, 1], [1, 0]], s.palindromePairs(["a", ""]))

        self.assertEqual([[0, 1], [1, 0]], s.palindromePairs(["a", "a"]))

        self.assertEqual(
            [[0, 1], [1, 0], [2, 4], [3, 2]],
            s.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]),
        )

        self.assertEqual([], s.palindromePairs(["abcd", "sssll"]))

        self.assertEqual([], s.palindromePairs([]))

        self.assertEqual([[0, 1], [1, 0]], s.palindromePairs(["bat", "tab", "cat"]))


if __name__ == "__main__":
    unittest.main()
