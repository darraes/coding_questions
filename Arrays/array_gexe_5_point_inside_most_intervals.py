#https://code.google.com/p/prep/wiki/ExercisesList

# Given a list of intervals [begini, endi], find a point which overlaps the most intervals

def find_point(intervals):
    flat_start = [(i[0], 1) for i in intervals]
    flat_end = [(i[1], -1) for i in intervals]

    flat = []
    flat.extend(flat_start)
    flat.extend(flat_end)

    flat.sort(lambda l, r: l[0] - r[0] if l[0] != r[0] else l[1] - r[1])

    max_point, max_sum, current_sum = 0, 0, 0

    for point in flat:
        current_sum += point[1]
        if current_sum > max_sum:
            max_sum = current_sum
            max_point = point[0]

    return max_point, max_sum

###############################################################
import unittest

class TestFunctions(unittest.TestCase):

    def test_simple_intervals(self):
        self.assertEqual((4, 4), find_point([(0, 5), (2, 6), (3, 7), (4, 8), (7, 13)]))        

if __name__ == '__main__':
    unittest.main()
