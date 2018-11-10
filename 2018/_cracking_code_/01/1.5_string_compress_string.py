def compress(input):
    result = ""
    i = 0
    while i < len(input):
        letter = input[i]
        count = 0
        while i < len(input) and letter == input[i]:
            count += 1
            i += 1
        # String concatenations in Python are very performant
        result += letter
        result += str(count)
    return result if len(result) < len(input) else input
   

###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEquals("a2b1c5a3", compress("aabcccccaaa"))
        self.assertEquals("abcd", compress("abcd"))


if __name__ == '__main__':
    unittest.main()