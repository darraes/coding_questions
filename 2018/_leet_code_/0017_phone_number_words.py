def generate_words(numbers):
    if not len(numbers):
        return []

    conv_map = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    state = [-1] * len(numbers)
    level = 0
    res = []

    def backtrack():
        nonlocal level, state, conv_map, numbers
        while True:
            state[level] = -1
            level -= 1
            if level < 0:
                return False
            if state[level] < len(conv_map[numbers[level]]) - 1:
                return True

    def form_word():
        nonlocal res, state, conv_map, numbers
        tmp = []
        for i in range(len(numbers)):
            tmp.append(conv_map[numbers[i]][state[i]])
        res.append("".join(tmp))

    while True:
        state[level] += 1
        if level < len(numbers) - 1:
            level += 1
        else:
            form_word()
            if state[level] < len(conv_map[numbers[level]]) - 1:
                continue
            if not backtrack():
                break

    return res


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        return generate_words(digits)


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], generate_words("23")
        )
        self.assertEqual(
            ["dd", "de", "df", "ed", "ee", "ef", "fd", "fe", "ff"], generate_words("33")
        )
        self.assertEqual(["w", "x", "y", "z"], generate_words("9"))
        self.assertEqual([], generate_words(""))


if __name__ == "__main__":
    unittest.main()
