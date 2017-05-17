from collections import Iterator

class TreeNode:
    def __init__(self, left, right, value):
        self._left = left
        self._right = right
        self._value = value

    def __eq__(self, other):
        if type(other) is type(self):
            return self._value == other._value
        return False

########## IN ORDER ###########################

def in_order(node):
    if node is None: return

    in_order(node._left)
    print node._value,
    in_order(node._right)


def in_order_iterative(node):
    visit = []
    stack = []
    
    # The idea is very similar to the recursive approach.
    # We keep going to the left as much as we can. Once we reach the limit
    # we will visit the node at the top of the stack.
    # After that, if we can go to the right of this last node, we will move to
    # the right.
    while len(stack) > 0 or node is not None:
        if node:
            stack.append(node)
            node = node._left
        else:
            element = stack.pop()
            visit.append(element._value)

            if element._right:
                node = element._right
    return visit


class InOrderIterator(Iterator):
    def __init__(self, node):
        self._node = node
        self._stack = []

    def next(self):
        while len(self._stack) > 0 or self._node:
            if self._node:
                self._stack.append(self._node)
                self._node = self._node._left
            else:
                next = self._stack.pop()
                if next._right:
                    self._node = next._right
                return next
        raise StopIteration


########## END IN ORDER ######################

########## PRE ORDER #########################

def pre_order(node):
    if node is None: return

    print node._value,
    pre_order(node._left)    
    pre_order(node._right)


def pre_order_iterative(node):
    visit = []
    stack = []
    stack.append(node)

    # Pre-order is the easiest iterative one. Once I node is pushed into the stack
    # we immediately consume it and put his right and then his left on the stack.
    while len(stack) > 0:
        element = stack.pop()
        visit.append(element._value)
        if element._right: 
            stack.append(element._right)
        if element._left: 
            stack.append(element._left)
    return visit


class PreOrderIterator(Iterator):
    def __init__(self, node):
        self._node = node
        self._stack = []
        self._stack.append(node)

    def next(self):
        while len(self._stack) > 0:
            next = self._stack.pop()
            if next._right: 
                self._stack.append(next._right)
            if next._left: 
                self._stack.append(next._left)
            return next
        raise StopIteration

########## END PRE ORDER ######################

########## POST ORDER #########################

def post_order(node):
    if node is None: return
    
    post_order(node._left)    
    post_order(node._right)
    print node._value,


def post_order_iterative(node):
    visit = []
    stack = []
    last_element = None

    # Post order is similar to in-order in the sense that we will add the current node
    # to the stack and move to it's left if we can.
    # When we get to the time of poping an element, we need to make sure that the last
    # element visited was his right, therefore we need to keep track of the last node
    # visited and do a peek before poping an element.
    while len(stack) > 0 or node:
        if node:
            stack.append(node)
            node = node._left
        else:
            element = stack[-1]
            # If there is a right and it was not the very last element visited
            # then it means we should go to right.
            # Otherwise, it means we have just visited the right element and therefore
            # it is time to visit the current element
            if element._right and element._right != last_element:            
                node = element._right
            else: # If we have just visited the elements right, it is the elements turn          
                visit.append(element._value)
                last_element =  stack.pop()

    return visit


class PostOrderIterator(Iterator):
    def __init__(self, node):
        self._node = node
        self._last_element = None
        self._stack = []

    def next(self):
        while len(self._stack) > 0 or self._node:
            if self._node:
                self._stack.append(self._node)
                self._node = self._node._left
            else:
                peek = self._stack[-1]
                if peek._right and peek._right != self._last_element:
                    self._node = peek._right
                else:
                    self._last_element = self._stack.pop()
                    return self._last_element
        raise StopIteration


########## END POST ORDER ######################


################ TESTS ########################################
###############################################################
import unittest

class TestFunctions(unittest.TestCase):

    def test_in_order(self):
        root = TreeNode(TreeNode(TreeNode(None, None, 30)
                               , TreeNode(None, None, 45)
                               , 40)
                      , TreeNode(TreeNode(None, None, 55)
                               , TreeNode(None, None, 70)
                               , 60)
                      , 50)

        r1 = in_order_iterative(root)
       
        r2 = []
        iterator = InOrderIterator(root)
        for node in iterator: r2.append(node._value)

        self.assertEqual(r1, r2)
        

    def test_pre_order(self):
        root = TreeNode(TreeNode(TreeNode(None, None, 30)
                               , TreeNode(None, None, 45)
                               , 40)
                      , TreeNode(TreeNode(None, None, 55)
                               , TreeNode(None, None, 70)
                               , 60)
                      , 50)

        r1 = pre_order_iterative(root)
        
        r2 = []
        iterator = PreOrderIterator(root)
        for node in iterator: r2.append(node._value)

        self.assertEqual(r1, r2)


    def test_post_order(self):
        root = TreeNode(TreeNode(TreeNode(None, None, 30)
                               , TreeNode(None, None, 45)
                               , 40)
                      , TreeNode(TreeNode(None, None, 55)
                               , TreeNode(None, None, 70)
                               , 60)
                      , 50)
        
        r1 = post_order_iterative(root)
        
        r2 = []
        iterator = PostOrderIterator(root)
        for node in iterator: r2.append(node._value)
        
        self.assertEqual(r1, r2)
        


if __name__ == '__main__':
    unittest.main()