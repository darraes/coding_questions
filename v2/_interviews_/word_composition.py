def find_compositive_words(words):
    words_set = set(words)
    memo = {}

    def dp(w):
        print(w)
        nonlocal memo
        if w == "":
            return (True, 0)

        if w in memo:
            return memo[w]

        memo[w] = (False, 0)

        for i in range(1, len(w) + 1):
            print(i, w[:i], w[i:])
            if w[:i] in words_set:
                sub_res, w_count = dp(w[i:])
                if sub_res:
                    memo[w] = (sub_res, 1 + w_count)
                break

        return memo[w]

    ans = []
    for w in words:
        res, w_count = dp(w)
        if res and w_count > 1:
            ans.append(w)

    return ans


def find_compositive_words_v2(words):
    words_set = set(words)
    memo = {}

    def dp(w):
        print(w)
        nonlocal memo
        if w == "":
            return True, []

        if w in memo:
            return memo[w]

        memo[w] = False, []

        for i in range(1, len(w) + 1):
            print(i, w[:i], w[i:])
            if w[:i] in words_set:
                found, sub_res = dp(w[i:])
                if found:
                    memo[w] = True, [w] + sub_res
                    break

        return memo[w]

    ans = []
    for w in words:
        res, parts = dp(w)
        if res and len(parts) > 1:
            ans.append(w)

    return ans


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            ["santamonica"],
            find_compositive_words_v2(
                ["santamonica", "santa", "monica", "santax", "venice"]
            ),
        )

        self.assertEqual(
            ["santamonica", "santavenice"],
            find_compositive_words_v2(
                ["santamonica", "santa", "monica", "santax", "venice", "santavenice"]
            ),
        )

        self.assertEqual(
            [], find_compositive_words_v2(["santa", "monica", "santax", "venice"])
        )

        self.assertEqual(
            ["santamonicavenice"],
            find_compositive_words_v2(
                ["santamonicavenice", "santa", "monica", "santax", "venice"]
            ),
        )

        self.assertEqual([], find_compositive_words_v2(["a", "b", "c"]))
        self.assertEqual(["abc"], find_compositive_words_v2(["a", "b", "c", "abc"]))


if __name__ == "__main__":
    unittest.main()
