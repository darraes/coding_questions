from collections import defaultdict


def get_key(word):
    return "".join(sorted(word))


def longest_path(words):
    anagrams = defaultdict(int)

    for word in words:
        key = get_key(word)
        anagrams[key] += 1

    ans = 0
    for word in words:
        ans = max(ans, longest_path_impl(word, words, anagrams, {}))
    return ans


def longest_path_impl(word, words, anagrams, cache):
    if word == "":
        return 0

    if word in cache:
        return cache[word]

    ans = 0
    for i in range(len(word)):
        ans = max(
            ans, longest_path_impl(word[:i] + word[i + 1:], words, anagrams, cache)
        )

    ans += anagrams[get_key(word)]

    cache[word] = ans
    return cache[word]


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            6,
            longest_path(
                ["alter", "later", "late", "facebook", "face", "tale", "ale", "teal"]
            ),
        )


if __name__ == "__main__":
    unittest.main()
