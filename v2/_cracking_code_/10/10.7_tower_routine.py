from collections import namedtuple

Person = namedtuple("Person", ["height", "weight"])


def max_possible_tower(artists):
    ''' 
    Longest Increasing Subsequence
    '''
    artists.sort(key=lambda p: p.height)
    
    gmax = 0
    dp = [0] * len(artists)
    dp[0] = 1
    for i in range(len(dp)):
        for j in range(i):
            cur_max = 1
            if artists[i].weight > artists[j].weight:
                cur_max = 1 + dp[j]
            dp[i] = max(dp[i], cur_max)
        gmax = max(gmax, dp[i])
    print(dp)
    return gmax


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            2, max_possible_tower([Person(80, 60), Person(70, 120), Person(65, 100)])
        )


if __name__ == "__main__":
    unittest.main()
