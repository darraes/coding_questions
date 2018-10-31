'''Problem
Given a expression string with numbers and the operators '+' and/or '*', find all possible results of the expression assuming you can add parenthesis to the expression as you may.
'''

from dy_utils import collection_equals

def explode(expression):
    def mul(a, b):
        result = set()
        for ea in a:
            for eb in b:
                result.add(int(ea) * int(eb))
        return set(result)

    def add(a, b):
        result = set()
        for ea in a:
            for eb in b:
                result.add(int(ea) + int(eb))
        return set(result)

    def explode_impl(expression, s, e, cache):
        key = "{},{}".format(s, e)
        if (cache.has_key(key)): return cache[key]
        
        results = set()
        if (s == e - 1): return expression[s]
        for i in range(e)[s:e - 1]:
            if (expression[i] == '+'):
                results.update(add(explode_impl(expression, s, i, cache),
                                   explode_impl(expression, i + 1, e, cache)))
            elif (expression[i] == '*'):
                results.update(mul(explode_impl(expression, s, i, cache),
                                   explode_impl(expression, i + 1, e, cache)))

        cache[key] = results
        return results

    return explode_impl(expression, 0, len(expression), dict())

###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_basic(self):
        results = sorted(explode("2+2*2"))
        self.assertTrue(collection_equals(results, [6, 8]))

        results = sorted(explode("1+1*1"))
        self.assertTrue(collection_equals(results, [2]))

        results = sorted(explode("1*1*1"))
        self.assertTrue(collection_equals(results, [1]))

        results = sorted(explode("3+3+2*4"))
        self.assertTrue(collection_equals(results, [14, 23, 32]))

if __name__ == '__main__':
    unittest.main()