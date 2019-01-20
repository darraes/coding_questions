class TrieNode:
    def __init__(self, is_end):
        self.is_end = is_end
        self.edges = {}


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(is_end=False)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        i = 0
        current_node = self.root
        while i < len(word):
            if word[i] not in current_node.edges:
                current_node.edges[word[i]] = TrieNode(is_end=False)
            current_node = current_node.edges[word[i]]
            i += 1
        current_node.is_end = True


class Solution:
    def findWords(self, board, words):
        res = set()

        def neighbors(i, j, used):
            nonlocal board
            return [
                (x, y)
                for (x, y) in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]
                if (x, y) not in used and 0 <= x < len(board) and 0 <= y < len(board[x])
            ]

        def search(node, i, j, used, path):
            nonlocal res, board

            if board[i][j] in node.edges:
                used.add((i, j))
                path.append(board[i][j])

                next_node = node.edges[board[i][j]]
                if next_node.is_end:
                    res.add("".join(path))

                for n_i, n_j in neighbors(i, j, used):
                    search(next_node, n_i, n_j, used, path)

                del path[-1]
                used.remove((i, j))

        trie = Trie()
        for w in words:
            trie.insert(w)

        for i in range(len(board)):
            for j in range(len(board[i])):
                search(trie.root, i, j, set(), [])

        return list(res)


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(set(["a"]), set(s.findWords([["a"]], ["a"])))

        self.assertEqual(
            set(["oath", "eat"]),
            set(
                s.findWords(
                    [
                        ["o", "a", "a", "n"],
                        ["e", "t", "a", "e"],
                        ["i", "h", "k", "r"],
                        ["i", "f", "l", "v"],
                    ],
                    ["oath", "pea", "eat", "rain"],
                )
            ),
        )

        self.assertEqual(
            [],
            s.findWords(
                [
                    ["o", "a", "a", "n"],
                    ["e", "t", "a", "r"],
                    ["i", "h", "k", "a"],
                    ["i", "f", "l", "v"],
                ],
                ["arara"],
            ),
        )

        self.assertEqual(
            [],
            s.findWords(
                [
                    ["o", "a", "a", "n"],
                    ["e", "t", "a", "r"],
                    ["i", "h", "k", "a"],
                    ["i", "f", "l", "r"],
                ],
                ["arara"],
            ),
        )

        self.assertEqual(
            ["arara"],
            s.findWords(
                [
                    ["o", "a", "a", "n"],
                    ["e", "t", "a", "r"],
                    ["i", "h", "k", "a"],
                    ["i", "f", "a", "r"],
                ],
                ["arara"],
            ),
        )


if __name__ == "__main__":
    unittest.main()
