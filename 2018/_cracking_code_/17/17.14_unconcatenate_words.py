from collections import deque
from copy import copy


def unconcatenate(s, words):
    sentence = list(unconcatenate_impl(s, words, 0, {})[1])
    return " ".join(sentence).strip()


def unconcatenate_impl(s, words, start, cache):
    if start >= len(s):
        return (0, deque())

    if start in cache:
        return cache[start]

    score, res = 0, deque()

    for i in range(start + 1, len(s) + 1):
        if i - start > 10:
            break

        _score, _res = unconcatenate_impl(s, words, i, cache)
        cur_word = s[start:i]
        add_score = 1 if cur_word in words else 0
        if _score + add_score >= score:
            res = copy(_res)
            res.appendleft(cur_word)
            score = _score + add_score

    cache[start] = (score, res)
    return (score, res)


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            "jess looked just like tim her brother",
            unconcatenate(
                "jesslookedjustliketimherbrother",
                ["looked", "just", "like", "her", "brother"],
            ),
        )


if __name__ == "__main__":
    unittest.main()
