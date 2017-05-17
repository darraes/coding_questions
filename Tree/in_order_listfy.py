# Cracking the code Interview - Moderate

class BiNode(object):

    def __init__(self, value, left, right):
        self._value = value
        self._left = left
        self._right = right

    def __str__(self):
        return "{}".format(self._value)
    
    @staticmethod
    def listfy(node):
        if node is None: 
            return None, None
        
        # Listfy the children first so the current node only needs to be 
        # inserted between the lists created from its children
        l_head = l_tail = r_head = r_tail = None
        if node._left:
            l_head, l_tail = BiNode.listfy(node._left)
        if node._right:
            r_head, r_tail = BiNode.listfy(node._right)
            
        if not l_tail and not r_head:
            return node, node
        else:
            # if there is a list to the left, the current node becomes 
            # the new tail of that list and the head of the full list remains 
            # the same. Otherwise, the current node is the head of the 
            # current list.
            if l_tail:
                l_tail._right = node
                node._left = l_tail
            else:
                l_head = node
            
            # If there is a list to the right, the current node becomes
            # the new head of that list and the tail of the full list remains
            # the same. Otherwise, the current node is the tail of the
            # the current list.
            if r_head:
                node._right = r_head
                r_head._left = node
            else:
                r_tail = node
                
        return l_head, r_tail
        

def print_list(node):
    str = ""
    while node is not None:
        str += "({}, {}, {}) -> ".format(node._left, node._value, node._right)
        node = node._right
    print str


###############################################################
import unittest

class TestFunctions(unittest.TestCase):

    def test_1(self):
        tree = BiNode(4
                    , BiNode(2, None, None)
                    , BiNode(6, None, None))
        head, tail = BiNode.listfy(tree)
        self.compare([2, 4, 6], head)
        
    def test_2(self):
        tree = BiNode(4
                    , BiNode(2
                           , BiNode(1, None, None)
                           , BiNode(3, None, None))
                    , BiNode(6
                           , BiNode(5, None, None)
                           , BiNode(7, None, None)))
        head, tail = BiNode.listfy(tree)
        self.compare([1, 2, 3, 4, 5, 6, 7], head)
        
    def test_3(self):
        tree = BiNode(4, None, None)
        head, tail = BiNode.listfy(tree)
        self.compare([4], head)
        
    def compare(self, values, node):
        print_list(node)
        previous = None
        i_value = 0
        while node:
            self.assertEquals(values[i_value], node._value)
            i_value += 1
            previous = node
            node = node._right
            
        i_value -= 1    
        while previous:
            self.assertEquals(values[i_value], previous._value)
            i_value -= 1
            previous = previous._left


if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    