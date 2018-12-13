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

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        i = 0
        current_node = self.root
        while i < len(word):
            if word[i] not in current_node.edges:
                return False
            else:
                current_node = current_node.edges[word[i]]
            i += 1
        return current_node.is_end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        i = 0
        current_node = self.root
        while i < len(prefix):
            if prefix[i] not in current_node.edges:
                return False
            else:
                current_node = current_node.edges[prefix[i]]
            i += 1
        return True


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

        self.assertTrue(trie.search("word"))
        self.assertFalse(trie.search("wor"))
        self.assertFalse(trie.search("worf"))
        self.assertFalse(trie.search("wording"))
        self.assertTrue(trie.search("face"))
        self.assertTrue(trie.search("facebook"))
        self.assertFalse(trie.search("faci"))
        self.assertTrue(trie.search("book"))
        self.assertTrue(trie.search("booking"))
        self.assertFalse(trie.search("bookin"))

        self.assertTrue(trie.startsWith("word"))
        self.assertTrue(trie.startsWith("wor"))
        self.assertTrue(trie.startsWith("boo"))
        self.assertTrue(trie.startsWith("booki"))
        self.assertTrue(trie.startsWith("fac"))
        self.assertTrue(trie.startsWith("faci"))
        self.assertTrue(trie.startsWith("face"))
        self.assertTrue(trie.startsWith("faceb"))
        self.assertTrue(trie.startsWith("wor"))
        self.assertFalse(trie.startsWith("worf"))
        self.assertFalse(trie.startsWith("wording"))


if __name__ == "__main__":
    unittest.main()
