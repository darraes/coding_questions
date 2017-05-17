# http://www.careercup.com/question?id=5669407776833536

# Write a program that answers YES/NO search queries containing * placeholders. 
# Example: if the data you have is (hazem, ahmed, moustafa, fizo), then you should 
# answer as follows for:

# m**stafa: yes
# fizoo: NO

# Your program should be able to answer each search query in O(1).

def query(words, query):
    keys = set()
    for word in words:
        tmp_keys = _create_word_keys(word)
        keys.update(tmp_keys)
        
    return query in keys
    
    
def _create_word_keys(str, i = 0):
    if len(str) - 1 == i:
        return [['*'], [str[i]]]
    
    # The DP call creates the keys for the subword starting at the next index
    # After that the current level result is built by deriving 2 new keys for
    # each sub key and appending '*' or this level char to the derived subkey
    level_result = []
    for subkey in _create_word_keys(str, i + 1):
        result = list(subkey)
        result.append('*')
        level_result.append(result)
        
        result = list(subkey)
        result.append(str[i])
        level_result.append(result)
    
    # Since we append to the end of the list to avoid shifts, at the very top
    # call we need to reverse all words
    if i == 0: return [''.join(r[::-1]) for r in level_result]    
    else: return level_result
    
    
###############################################################
import unittest

class TestFunctions(unittest.TestCase):

    def test_1(self):
        self.assertEqual(True, query(["test"], "t*st"))

    def test_problem(self):
        self.assertEqual(True, query(["hazem", "ahmed", "moustafa", "fizo"], "m**stafa"))


if __name__ == '__main__':
    unittest.main()

        
    