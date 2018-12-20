def gen_subsets(elements):
    def _gen_subsets(elements, level, subset):
        if level == len(elements):
            # print(subset)
            return

        _gen_subsets(elements, level + 1, subset)
        _gen_subsets(elements, level + 1, subset + [elements[level]])

    _gen_subsets(elements, 0, [])


def gen_subsets2(array):
    if len(array) == 0:
        return [[]]

    children = gen_subsets2(array[1:])

    res = []
    for subset in children:
        res.append(subset + [])
        res.append(subset + [array[0]])

    return res


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        gen_subsets([1, 2, 3])
        print(gen_subsets2([1, 2, 3]))


if __name__ == "__main__":
    unittest.main()
