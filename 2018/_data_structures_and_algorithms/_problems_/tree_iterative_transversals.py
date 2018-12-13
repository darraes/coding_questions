from tree_utils import TreeNode, pretty_print, friendly_build, tree_equals, tnode

########## IN ORDER ###########################

def in_order(node):
    if node is None: return

    in_order(node._left)
    print node._value,
    in_order(node._right)


def in_order_iterative(node):
    pass


class InOrderIterator(Iterator):
    def __init__(self, node):
        pass


########## END IN ORDER ######################

########## PRE ORDER #########################

def pre_order(node):
    if node is None: return

    print node._value,
    pre_order(node._left)    
    pre_order(node._right)


def pre_order_iterative(node):
    pass


class PreOrderIterator(Iterator):
    def __init__(self, node):
        pass

########## END PRE ORDER ######################

########## POST ORDER #########################

def post_order(node):
    if node is None: return
    
    post_order(node._left)    
    post_order(node._right)
    print node._value,


def post_order_iterative(node):
    pass


class PostOrderIterator(Iterator):
    def __init__(self, node):
        pass


########## END POST ORDER ######################