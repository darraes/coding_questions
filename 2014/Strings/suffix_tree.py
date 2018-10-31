# Cracking the Code Interview - 18.8

class SuffixTree(object):
    def __init__(self, word):
        self._map = dict()
        self._word = word

        for i in range(len(word)):
            if not self._map.has_key(word[i]):
                self._map[word[i]] = TrieNode(word[i])
            if i < len(word) - 1:
                self._map[word[i]].add(word[i:])

    def exists(self, word):
        if not self._map.has_key(word[0]): return False
        return self._map[word[0]].has_path(word)


class TrieNode(object):
    def __init__(self, char):
        self._map = dict()
        self._char = char

    def add(self, word):
        if word is None or len(word) == 0: return
        if self._char != word[0]: raise ValueError("Wrong Branch")

        if len(word) > 1:
            if not self._map.has_key(word[1]):
                self._map[word[1]] = TrieNode(word[1])

            self._map[word[1]].add(word[1:])

    def has_path(self, word):
        if word is None or len(word) == 0: return True
        if self._char != word[0]: return False
        if len(word) == 1: return True
        if not self._map.has_key(word[1]): return False

        return self._map[word[1]].has_path(word[1:])

st = SuffixTree("bibs")
print st.exists("ibs")
print st.exists("ib")
print st.exists("bib")
print st.exists("iba")