def unique_chars(text):
    tracker = {}
    for letter in text:
        if letter not in tracker:
            tracker[letter] = 0
        
        tracker[letter] += 1

        if tracker[letter] > 1:
            return False
    return True
   

###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertFalse(unique_chars("aabcccccaaa"))
        self.assertTrue(unique_chars("abcd"))


if __name__ == '__main__':
    unittest.main()