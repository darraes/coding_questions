from collections import namedtuple

Box = namedtuple("Box", ["w", "h", "d"])


def smaller(b1, b2):
    return b1.w < b2.w and b1.h < b2.h and b1.d < b2.d


def tallest(base, boxes, used, memo):
    max_h = 0

    if base in memo:
        return memo[base]

    for b in [b for b in boxes if b not in used]:
        if not base or smaller(b, base):
            used.add(b)
            height = tallest(b, boxes, used, memo)
            used.remove(b)

            max_h = max(max_h, height)

    cur_height = max_h + (base.h if base else 0)
    memo[base] = cur_height
    return cur_height


def solve(boxes):
    return tallest(None, boxes, set(), {})


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(6, solve([Box(1, 1, 1), Box(2, 2, 2), Box(3, 3, 3)]))
        self.assertEqual(5, solve([Box(1, 1, 1), Box(1, 2, 2), Box(3, 3, 3)]))
        self.assertEqual(3, solve([Box(1, 2, 3), Box(2, 3, 1), Box(3, 2, 1)]))
        self.assertEqual(4, solve([Box(1, 1, 1), Box(2, 3, 2), Box(3, 3, 3)]))


if __name__ == "__main__":
    unittest.main()
