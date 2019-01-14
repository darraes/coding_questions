def parenthesis(n):
    def _parenthesis(n, cur_i, left, right, p, results):
        if cur_i == 2 * n:
            results.append("".join(p))

        if left < n:
            left += 1
            _parenthesis(n, cur_i + 1, left, right, p + ["("], results)
            left -= 1
        if right < left:
            right += 1
            _parenthesis(n, cur_i + 1, left, right, p + [")"], results)
            right -= 1

    results = []
    _parenthesis(n, 0, 0, 0, [], results)
    return results

####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        print(parenthesis(1))
        print(parenthesis(2))
        print(parenthesis(3))


if __name__ == "__main__":
    unittest.main()