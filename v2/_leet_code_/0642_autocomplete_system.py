from heapq import heappop, heappush

class HeapNode:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        if self.priority != other.priority:
            return self.priority < other.priority
        else:
            return self.data > other.data


class TrieNode:
    def __init__(self, hits):
        self.hits = hits
        self.edges = {}


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(hits=0)

    def insert(self, word, hits):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        i = 0
        current_node = self.root
        while i < len(word):
            if word[i] not in current_node.edges:
                current_node.edges[word[i]] = TrieNode(hits=0)
            current_node = current_node.edges[word[i]]
            i += 1
        current_node.hits += hits

    def starts_with(self, prefix, max_return):
        heap = []

        def _add_all(prefix, node):
            nonlocal heap, max_return
            if node.hits:
                heappush(heap, HeapNode(prefix, node.hits))
                if len(heap) > max_return:
                    heappop(heap)

            for c, next_node in node.edges.items():
                _add_all(prefix + c, next_node)

        i = 0
        current_node = self.root

        while i < len(prefix):
            if prefix[i] not in current_node.edges:
                return []

            current_node = current_node.edges[prefix[i]]
            i += 1

        _add_all(prefix, current_node)

        ans = []
        while len(heap) > 0:
            ans.append(heappop(heap).data)

        return ans[::-1]


class AutocompleteSystem:
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.current_word = ""
        self.trie = Trie()
        for i in range(len(sentences)):
            self.trie.insert(sentences[i], times[i])

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c != "#":
            self.current_word += c
            return self.trie.starts_with(self.current_word, 3)
        else:
            self.trie.insert(self.current_word, 1)
            self.current_word = ""
            return []


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        autocomplete = AutocompleteSystem(
            ["i love you", "island", "ironman", "i love leetcode"], [5, 3, 2, 2]
        )

        self.assertEqual(
            ["i love you", "island", "i love leetcode"], autocomplete.input("i")
        )
        self.assertEqual(
            ["i love you","i love leetcode"], autocomplete.input(" ")
        )
        self.assertEqual(
            [], autocomplete.input("a")
        )
        self.assertEqual(
            [], autocomplete.input("#")
        )

        self.assertEqual(
            ["i love you", "island", "i love leetcode"], autocomplete.input("i")
        )
        self.assertEqual(
            ["i love you","i love leetcode", "i a"], autocomplete.input(" ")
        )
        self.assertEqual(
            ["i a"], autocomplete.input("a")
        )
        self.assertEqual(
            [], autocomplete.input("#")
        )


if __name__ == "__main__":
    unittest.main()
