from tree_utils import TreeNode, pretty_print, friendly_build, tree_equals, tnode
from collections import Iterator

########## IN ORDER ###########################

def in_order(node, ans):
    if node is None: return

    in_order(node.left, ans)
    ans.append(node.value)
    in_order(node.right, ans)


def in_order_iterative(node):
    ans = []
    stack = []
    while node or len(stack) > 0:
        if node:
            stack.append(node)
            node = node.left
        else:
            element = stack.pop()
            ans.append(element.value)
            node = element.right
    return ans


class InOrderIterator(Iterator):
    def __init__(self, node):
        self.stack = []
        self.current = node

    def __next__(self):
        while self.current or len(self.stack) > 0:
            if self.current:
                self.stack.append(self.current)
                self.current = self.current.left
            else:
                element = self.stack.pop()
                self.current = element.right
                return element.value
        raise StopIteration


########## END IN ORDER ######################

########## PRE ORDER #########################

def pre_order(node, ans):
    if node is None: return

    ans.append(node.value)
    pre_order(node.left, ans)    
    pre_order(node.right, ans)


def pre_order_iterative(node):
    ans = []
    stack = []

    while node or len(stack) > 0:
        if node:
            ans.append(node.value)
            stack.append(node)
            node = node.left
        else:
            element = stack.pop()
            node = element.right

    return ans


class PreOrderIterator(Iterator):
    def __init__(self, node):
        self.stack = []
        self.current = None

    def __next__(self):
        while self.current or len(self.stack) > 0:
            if self.current:
                self.stack.append(self.current)
                self.current = self.current.left
                return self.current.value
            else:
                element = self.stack.pop()
                self.current = element.right
        raise StopIteration

########## END PRE ORDER ######################

########## POST ORDER #########################

def post_order(node, ans):
    if node is None: return
    
    post_order(node.left, ans)    
    post_order(node.right, ans)
    ans.append(node.value)


def post_order_iterative(node):
    pass


class PostOrderIterator(Iterator):
    def __init__(self, node):
        self.stack = []
        self.current = None

    def next(self):
        pass


########## END POST ORDER ######################


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_in_order(self):
        root = friendly_build(
            [
                ["7"],
                ["10", "2"],
                ["4", "3", "8", "N"],
                ["N", "N", "N", "1", "11", "N", "N", "N"],
            ]
        )

        in_buf = []
        in_order(root, in_buf)
        self.assertEqual(in_buf, in_order_iterative(root))

        ite_res = []
        ite = InOrderIterator(root)
        for value in ite: 
            ite_res.append(value)

        self.assertEqual(in_buf, ite_res)

    def test_pre_order(self):
        root = friendly_build(
            [
                ["7"],
                ["10", "2"],
                ["4", "3", "8", "N"],
                ["N", "N", "N", "1", "11", "N", "N", "N"],
            ]
        )

        pre_buf = []
        pre_order(root, pre_buf)
        self.assertEqual(pre_buf, pre_order_iterative(root))

        ite_res = []
        ite = PreOrderIterator(root)
        for value in ite: 
            ite_res.append(value)

        self.assertEqual(pre_buf, ite_res)


    def test_post_order(self):
        return
        root = friendly_build(
            [
                ["7"],
                ["10", "2"],
                ["4", "3", "8", "N"],
                ["N", "N", "N", "1", "11", "N", "N", "N"],
            ]
        )

        post_buf = []
        post_order(root, post_buf)
        self.assertEqual(post_buf, post_order_iterative(root))

        


if __name__ == "__main__":
    unittest.main()