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
                child = TrieNode(is_end=False)
                current_node.edges[word[i]] = child
                current_node = child
            else:
                current_node = current_node.edges[word[i]]
            i += 1
        current_node.is_end = True


    def starts_with(self, prefix):
        ans = []
        def _add_all(prefix, node):
            nonlocal ans
            if node.is_end:
                ans.append(prefix)

            for c, next_node in node.edges.items():
                _add_all(prefix + c, next_node)

        i = 0
        current_node = self.root

        while i < len(prefix):
            if prefix[i] not in current_node.edges:
                return ans

            current_node = current_node.edges[prefix[i]]
            i += 1

        _add_all(prefix, current_node)
        return ans


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        trie = Trie()
        trie.insert("word")
        trie.insert("facebook")
        trie.insert("face")
        trie.insert("facing")
        trie.insert("book")
        trie.insert("booking")

        self.assertEqual(["word"], trie.starts_with("word"))
        self.assertEqual(["word"], trie.starts_with("wor"))
        self.assertEqual(["book", "booking"], trie.starts_with("boo"))
        self.assertEqual(["booking"], trie.starts_with("booki"))
        self.assertEqual(["face", "facebook"], trie.starts_with("face"))
        self.assertEqual(["face", "facebook", "facing"], trie.starts_with("fac"))
        self.assertEqual([], trie.starts_with("worf"))
        self.assertEqual(["facing"], trie.starts_with("faci"))


if __name__ == "__main__":
    unittest.main()
