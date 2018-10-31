# http://www.careercup.com/question?id=5090679891951616

# Given a pattern and a string, check whether the string matches the pattern. 
# For example: pattern "aba" and the string is "redblackred" then it matches 
# because "a" is translated to red and "b" is translated to "black". 
# Note that for eac

def match(pattern, str):
    matches = dict()
    return _match(pattern[:], str, 0, 0, matches), matches
    
def _match(pattern, str, current_ptrn, str_start, matches):
    if current_ptrn == len(pattern):
        if str_start == len(str): 
            return True
        else: 
            return False

    if pattern[current_ptrn] in matches:
        for str_end in range(str_start + 1, len(str) + 1):
            if matches[pattern[current_ptrn]] == str[str_start:str_end]:
                if _match(pattern, str, current_ptrn + 1, str_end, matches):
                    return True
    else:
        for str_end in range(str_start + 1, len(str) + 1):
            matches[pattern[current_ptrn]] = str[str_start:str_end]
            if _match(pattern, str, current_ptrn + 1, str_end, matches):
                return True
            del matches[pattern[current_ptrn]]
    
    return False


###############################################################
import unittest

class TestFunctions(unittest.TestCase):

    def test_simple(self):
        self.perform_test(True, "aba", "redblackred")
        self.perform_test(True, "abc", "redblackred")
        self.perform_test(True, "aaa", "redredred")
        self.perform_test(True, "abba", "redbluebluered")
        self.perform_test(True, "abbca", "redbluebluedred")
        self.perform_test(False, "aaa", "redredreda")
        self.perform_test(False, "aaa", "aredredred")
        self.perform_test(False, "aaa", "redredared")
        self.perform_test(False, "aaa", "r")
        self.perform_test(False, "aaa", "re")
        self.perform_test(False, "aaa", "")
        self.perform_test(False, "abc", "r")
        self.perform_test(False, "abc", "re")
        self.perform_test(False, "abc", "")
        self.perform_test(False, "aaaa", "redbluebluered")
        
        
    def perform_test(self, expected, pattern, str):
        result = match(pattern, str)
        print result
        self.assertEquals(expected, result[0])


if __name__ == '__main__':
    unittest.main()
            
                