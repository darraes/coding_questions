class TrieNode:
    def __init__(self, is_end):
        self.edges = {}
        self.is_end = is_end
        self.word_idx = -1


class Trie:
    def __init__(self):
        self.root = TrieNode(is_end=False)

    def insert(self, term, word_idx):
        current = self.root

        idx = 0
        while idx < len(term):
            if term[idx] not in current.edges:
                current.edges[term[idx]] = TrieNode(is_end=False)
            current = current.edges[term[idx]]
            idx += 1

        current.is_end = True
        current.word_idx = word_idx

    def list_tails(self, term, my_idx):
        current = self.root

        idx = 0
        while idx < len(term):
            if term[idx] not in current.edges:
                return False, []
            current = current.edges[term[idx]]
            idx += 1

        def get_all(current, start):
            nonlocal my_idx
            ans = []
            if current.is_end and my_idx != current.word_idx:
                ans.append(([start], current.word_idx))

            for edge, node in current.edges.items():
                sub_ans = get_all(node, edge)
                for sub in sub_ans:
                    if start != "":
                        sub[0].append(start)
                    ans.append(sub)

            return ans

        return True, get_all(current, "")


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
            has_results, results = trie.list_tails(word, i)
            if has_results:
                for (letters, word_idx) in results:
                    if self.isPalindrome(letters):
                        ans.append([i, word_idx])
        return ans


    def isPalindrome(self, letters):
        s = 0
        e = len(letters) - 1

        while s < e:
            if letters[s] != letters[e]:
                return False
            s += 1
            e -= 1
        return True


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertEqual(
            [[0, 1], [1, 0], [2, 4], [3, 2]],
            s.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]),
        )


if __name__ == "__main__":
    unittest.main()
