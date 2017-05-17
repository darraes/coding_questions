# Given a array of houses and 3 colors and a function that given a house 
# and a color, gives you the cost of painting. Find the minor cost to paint 
# the houses in such a way that neighbor houses don't share the same color.

# Houses can be structed as an array where each house is in its position

import sys

def paint_cost(house, color, cost):
    return cost[(house, color)]

def paint_houses(houses, index, colors, last_color, cache, cost):
    if index == len(houses): 
        return 0, []   
    if cache.has_key((index, last_color)): 
        return cache[(index, last_color)]

    min_cost = sys.maxint
    min_scheme = []
    for color in colors:
        if color != last_color:            
            sub_cost, sub_result = paint_houses(houses, index + 1, colors, color, cache, cost)
            current_cost = sub_cost + paint_cost(houses[index], color, cost)
            if current_cost < min_cost:
                min_cost = current_cost
                min_scheme = sub_result[:]
                min_scheme.insert(0, color)

    cache[(index, last_color)] = min_cost, min_scheme
    return  min_cost, min_scheme

###############################################################
import unittest

class TestFunctions(unittest.TestCase):

    def test_basic(self):
        cost_function = { (1, 1): 3,(1, 2): 1, (1, 3): 7,
                          (2, 1): 30,(2, 2): 6, (2, 3): 2,
                          (3, 1): 1,(3, 2): 16, (3, 3): 13,
                          (4, 1): 9,(4, 2): 8, (4, 3): 2,
                          (5, 1): 11,(5, 2): 1, (5, 3): 32,
                          (6, 1): 3,(6, 2): 1, (6, 3): 7 }

        cost, scheme = paint_houses([1, 2, 3, 4, 5, 6], 0, [1, 2, 3], 0, dict(), cost_function)
        self.assertEqual(10, cost)
        self.assertEqual([2, 3, 1, 3, 2, 1], scheme)

        cost, scheme = paint_houses([1, 2, 3, 4, 5, 6], 0, [1, 2], 0, dict(), cost_function)
        self.assertEqual(30, cost)
        self.assertEqual([1, 2, 1, 2, 1, 2], scheme)



if __name__ == '__main__':
    unittest.main()


