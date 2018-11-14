def _min_worst_egg_drop(eggs, floors, cache):
    if eggs == 1 or floors in [0, 1]:
        return (floors, 1)

    if (eggs, floors) in cache:
        return cache[(eggs, floors)]

    min_worst = 2**32 - 1
    jump = 0
    for i in range(1, floors + 1):
        local_worst = max(_min_worst_egg_drop(eggs, floors - i, cache)[0],
                          _min_worst_egg_drop(eggs - 1, i - 1, cache)[0])

        if local_worst < min_worst:
            min_worst = local_worst
            jump = i

    cache[(eggs, floors)] = (min_worst + 1, jump)
    return (min_worst + 1, jump)


def min_worst_egg_drop(eggs, floors):
    return _min_worst_egg_drop(eggs, floors, {})


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual((4, 4), min_worst_egg_drop(2, 10))
        self.assertEqual((14, 9), min_worst_egg_drop(2, 100))


if __name__ == '__main__':
    unittest.main()