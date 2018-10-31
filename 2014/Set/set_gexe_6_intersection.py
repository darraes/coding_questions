#https://code.google.com/p/prep/wiki/ExercisesList

# Given a group of sets, find the intersection between them without using a hash-table

def intersection(sets):
    result = sets[0]
    current = set()
    
    for s in sets[1:]:
        current = result
        result = set()
        for e in s:
            if e in current:
                result.add(e)
    return result

###############################################################
import unittest

class TestFunctions(unittest.TestCase):

    def test_bvt(self):
        self.assertEqual({3, 4, 5}, intersection([{3, 4, 5, 67, 78}, 
                                                  {3, 4, 5, 1, 2}, 
                                                  {3, 4, 5, 7, 8}]))

    def test_empty(self):
        self.assertEqual(set(), intersection([{67, 78}, 
                                           {1, 2}, 
                                           {3, 4, 5, 7, 8}]))

if __name__ == '__main__':
    unittest.main()