# http://www.careercup.com/question?id=5085545090777088

# Given a string containing letter, digit, and other characters, 
# write a function to check palindrome for only letter and digit. 
# The implementation need to be in-place, no extra memory is allowed 
# to create another string or array. 
# For example: 

# "ABA" is palindrome 
# "A!#A" is palindrome 
# "A man, a plan, a canal, Panama!" is palindrome

def is_alpha_palindrome(str):
    if not str:
        return True
        
    chars = str[:]
    start, end = 0, len(chars) - 1
    
    # The idea is to use 2 indexes and move index 1 from start to end and 
    # index 2 from end to start.
    # Every time both indexes find a alpha char, those must be compared.
    while True:
        while start < len(chars) and not chars[start].isalnum():
            start += 1
        while end >= 0 and not chars[end].isalnum():
            end -= 1
        
        # If pointers crossed, no news chars to look at
        if start > end:
            return True
        if chars[start].lower() != chars[end].lower():
            return False
        
        # Move both pointers ahead otherwise we will be in a infinite loop    
        start, end = start + 1, end - 1
            
            
##########################################################################
import unittest

class Tests (unittest.TestCase):

    def test_bvt(self):
        self.assertEquals(True, is_alpha_palindrome(""))
        self.assertEquals(True, is_alpha_palindrome(None))
        self.assertEquals(False, is_alpha_palindrome("A!#cBA"))
        self.assertEquals(True, is_alpha_palindrome("ABA"))
        self.assertEquals(True, is_alpha_palindrome("A!#A"))
        self.assertEquals(True, is_alpha_palindrome("A man, a plan, a canal, Panama!"))
        self.assertEquals(False, is_alpha_palindrome("A man, a pplan, a canal, Panama!"))
        		           

if __name__ == "__main__":
    unittest.main()
    