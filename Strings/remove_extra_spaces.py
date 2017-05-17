# http://www.careercup.com/question?id=5178446623801344

#Given a string with multiple spaces write a function to in-place trim all spaces leaving a single space between words 
#e.g. 
#_ _ _ Hello _ _ _ World _ _ _ 
#Hello _ World _ _ _ _ _ _ _ _ _

def remove_extra_spaces(str):
    c = p = 0
    while c < len(str) and p < len(str):        
        p = c
        while p < len(str) and str[p] == ' ': p += 1

        while p < len(str) and str[p] != ' ':
            if c != p:
                str[c] = str[p]
                str[p] = ' '
            p += 1
            c += 1        
        c += 1

    return str[:]

## Step solution




###############################################################
import unittest

class TestFunctions(unittest.TestCase):

    def test_basic(self):
        result = remove_extra_spaces([' ', ' ',' ','H','e','l','l','o',' ',' ','W','o','r','l','d',' ',' ',' ',' '])
        self.assertEqual(['H','e','l','l','o',' ','W','o','r','l','d',' ',' ',' ',' ', ' ', ' ',' ',' '], result)

        result = remove_extra_spaces(['H','e','l','l','o',' ','W','o','r','l','d',' ','W','o','r','l','d'])
        self.assertEqual(['H','e','l','l','o',' ','W','o','r','l','d',' ','W','o','r','l','d'], result)

        result = remove_extra_spaces(['H','e','l','l','o',' ',' ','o','r','l','d',' ','W','o','r','l','d'])
        self.assertEqual(['H','e','l','l','o',' ','o','r','l','d',' ','W','o','r','l','d', ' '], result)

        result = remove_extra_spaces(['H','e','l','l','o',' ','o','r','l','d',' ','W','o','r','l','d',' '])
        self.assertEqual(['H','e','l','l','o',' ','o','r','l','d',' ','W','o','r','l','d',' '], result)

if __name__ == '__main__':
    unittest.main()

