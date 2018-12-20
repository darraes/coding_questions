
def climb_ways(n, cache):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n in cache:
        return cache[n]

    cache[n] = climb_ways(n - 1, cache) \
               + climb_ways(n - 2, cache) \
               + climb_ways(n - 3, cache)
    return cache[n]


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEquals(4, climb_ways(3, {}))


if __name__ == '__main__':
    unittest.main()