import copy

coins = [25, 10, 5, 1]

def _ways_for_change(n, coin_idx, cache, cur_coin_count, solutions):
    if coins[coin_idx] == 1:
        cur_coin_count[coins[coin_idx]] = n
        solutions.append(copy.copy(cur_coin_count))
        return 1

    if n in cache:
        cache[n]

    res = 0;
    while True:
        res += _ways_for_change(
            n, coin_idx + 1, cache, cur_coin_count, solutions)
        n -= coins[coin_idx]
        cur_coin_count[coins[coin_idx]] += 1

        if n < 0:
            break

    cur_coin_count[coins[coin_idx]] = 0
    cache[n] = res
    return res

def ways_for_change(n):
    solutions = []
    res = _ways_for_change(n, 0, {}, {25: 0, 10: 0, 5: 0, 1: 0}, solutions)
    for s in solutions:
        print(s)
    return res

###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(13, ways_for_change(25))
        self.assertEqual(4, ways_for_change(11))


if __name__ == '__main__':
    unittest.main()