# Cracking the code interview

class TreeNode:
    def __init__(self, left, right, value):
        self._left = left
        self._right = right
        self._value = value

    def __eq__(self, other):
        if type(other) is type(self):
            return self._value == other._value
        return False

    def __str__(self):
        return "{}".format(self._value)

def find(root, q, x):
    if root is None:
        return (None, None, None)
    elif q == root or x == root:
        pl, ql, xl = find(root._left, q, x)
        pr, qr, xr = find(root._right, q, x)

        if q == root and (xl is not None or xr is not None):
            return (q, root, xl if xl is not None else xr)
        elif x == root and (ql is not None or ql is not None):
            return (x, ql if ql is not None else qr, root)
        else:
            return (None, root if q == root else None, root if x == root else None)
    else:
        pl, ql, xl = find(root._left, q, x)
        pr, qr, xr = find(root._right, q, x)

        if pl is not None:
            return (pl, ql, xl)
        if pr is not None:
            return (pr, qr, xr)

        if ql is not None and xr is not None:
            return (root, ql, xr)
        if qr is not None and xl is not None:
            return (root, qr, xl)

        return (None, ql if ql is not None else qr, xl if xl is not None else xr)


root = TreeNode(TreeNode(TreeNode(None, None, 49), None, 112), TreeNode(TreeNode(None, TreeNode(None, None, 5), 34), TreeNode(None, None, 16), 78), 4)

print find(root, TreeNode(None, None, 78), TreeNode(None, None, 16))[0]
