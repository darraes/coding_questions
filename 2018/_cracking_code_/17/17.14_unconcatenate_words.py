from collections import deque
from copy import copy


def unconcatenate(s, words):
    res = unconcatenate_impl(s, words, 0, {})
    print(res)
    sentence = list(res[2])
    return " ".join(sentence).strip()


def unconcatenate_impl(s, words, start, cache):
    if start >= len(s):
        return (0, 0, deque())

    if start in cache:
        return cache[start]

    score, mismatches, res = 0, 0, deque()

    for i in range(start + 1, len(s) + 1):
        if i - start > 10:
            break

        cur_word = s[start:i]
        _score, _mismatches, _res = unconcatenate_impl(s, words, i, cache)
        add_score, add_mismatches = (1, 0) if cur_word in words else (0, 1)
        if _score + add_score >= score:
            res = copy(_res)
            res.appendleft(cur_word)
            score = _score + add_score
            mismatches = _mismatches + add_mismatches

    cache[start] = (score, mismatches, res)
    return (score, mismatches, res)


def unconcatenate_by_misses(s, words):
    res = unconcatenate_by_misses_impl(s, words, 0, {})
    print(res)
    sentence = list(res[1])
    return " ".join(sentence).strip()


def unconcatenate_by_misses_impl(s, words, start, cache):
    if start >= len(s):
        return (0, deque())

    if start in cache:
        return cache[start]

    mismatches, res = 100000, deque()

    for i in range(start + 1, len(s) + 1):
        if i - start > 10:
            break

        cur_word = s[start:i]
        _mismatches, _res = unconcatenate_by_misses_impl(s, words, i, cache)
        add_mismatches = 0 if cur_word in words else 1
        if _mismatches + add_mismatches < mismatches:
            res = copy(_res)
            res.appendleft(cur_word)
            mismatches = _mismatches + add_mismatches

    cache[start] = (mismatches, res)
    return (mismatches, res)


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

        self.assertEqual(
            "jess looked just like tim her brother",
            unconcatenate_by_misses(
                "jesslookedjustliketimherbrother",
                ["looked", "just", "like", "her", "brother"],
            ),
        )


if __name__ == "__main__":
    unittest.main()
