class CompressedTrieNode(object):
    def __init__(self, is_end):
        self.children = {}
        self.edges = {}
        self.is_end = is_end


class CompressedTrie(object):
    def __init__(self):
        self.root = CompressedTrieNode(is_end=False)

    def insert(self, word):
        current_node = self.root
        i = 0

        while i < len(word):
            if word[i] not in current_node.edges:
                # Case 1: No path starting with that letter (New)
                current_node.edges[word[i]] = word[i:]
                current_node.children[word[i]] = CompressedTrieNode(is_end=True)

            else:
                idx = i
                j = 0
                label = current_node.edges[word[i]]
                while j < len(label) and i < len(word) and word[i] == label[j]:
                    j += 1
                    i += 1

                if j == len(label):
                    # Case 2: Label is a prefix of the word
                    # E.g. label=face, word=facebook
                    # face      facebook
                    #     ^     ^   ^
                    #     j   idx   i
                    
                    current_node = current_node.children[word[idx]]
                    if i == len(word):
                        # Case 3: Label and word are the same 
                        # face      face
                        #     ^     ^   ^
                        #     j   idx   i
                        current_node.is_end = True
                        return
                else:
                    if i == len(word):
                        # Case 4: word is a prefix of the label
                        # E.g. label=facebook, word=face
                        # State:
                        # facebook      face
                        #     ^         ^   ^
                        #     j       idx   i

                        existing = current_node.children[word[idx]]
                        new_child = CompressedTrieNode(is_end=True)

                        # Adding "face" edge to current node
                        current_node.edges[word[idx]] = word[idx:]
                        current_node.children[word[idx]] = new_child

                        # Adding "book" to new child
                        new_child.edges[label[j]] = label[j:]
                        new_child.children[label[j]] = existing
                    else:
                        # Case 5: word is partial match of label.
                        # E.g. label=facebook, word=facing
                        # State:
                        # facebook      facing
                        #    ^          ^  ^
                        #    j        idx  i

                        existing = current_node.children[word[idx]]
                        new_child = CompressedTrieNode(is_end=False)

                        # Adding "fac" edge to current node
                        current_node.edges[word[idx]] = word[idx:i]
                        current_node.children[word[idx]] = new_child

                        # Adding "ebook" to new child
                        new_child.edges[label[j]] = label[j:]
                        new_child.children[label[j]] = existing

                        # Adding "ing" to new child
                        new_child.edges[word[i]] = word[i:]
                        new_child.children[word[i]] = CompressedTrieNode(is_end=True)
                    return

    def print_trie(self):
        def _print_trie(node, level):
            for i, edge in node.edges.items():
                print(
                    "".join(2 * level * [" "]),
                    edge,
                    "({})".format(1 if node.children[i].is_end else 0),
                )
                _print_trie(node.children[i], level + 1)

        _print_trie(self.root, 0)


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        trie = CompressedTrie()

        trie.insert("facebook")
        trie.insert("face")
        trie.insert("this")
        trie.insert("there")
        trie.insert("then")
        trie.insert("the")
        trie.insert("facing")
        trie.insert("factory")

        trie.print_trie()

        # self.assertTrue(trie.search("there"))
        # self.assertFalse(trie.search("therein"))
        # self.assertTrue(trie.startsWith("th"))
        # self.assertFalse(trie.startsWith("fab"))

    def test_2(self):
        trie = CompressedTrie()

        trie.insert("factory")
        trie.insert("facing")
        trie.insert("the")
        trie.insert("then")
        trie.insert("there")
        trie.insert("this")
        trie.insert("face")
        trie.insert("facebook")

        trie.print_trie()

        # self.assertTrue(trie.search("there"))
        # self.assertFalse(trie.search("therein"))
        # self.assertTrue(trie.startsWith("th"))
        # self.assertFalse(trie.startsWith("fab"))


if __name__ == "__main__":
    unittest.main()
