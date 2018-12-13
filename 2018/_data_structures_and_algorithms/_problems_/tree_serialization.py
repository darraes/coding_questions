from tree_utils import TreeNode, pretty_print, friendly_build, tree_equals, tnode

def serialize_pre(node, buf):
    if not node:
        return

    buf.append(node.value)
    serialize_pre(node.left, buf)
    serialize_pre(node.right, buf)

def serialize_in(node, buf):
    if not node:
        return

    serialize_in(node.left, buf)
    buf.append(node.value)
    serialize_in(node.right, buf)


def build_from_in_pre(pre_order, in_order):
    pre_i = 0
    lookup = {}
    for i, e in enumerate(in_order):
        lookup[e] = i

    def _build_from_in_pre(pre_order, in_order, in_s, in_e):
        nonlocal pre_i, lookup
        if in_s > in_e:
            return None

        node = tnode(pre_order[pre_i])
        pre_i += 1
        if in_s != in_e:
            node.left = _build_from_in_pre(
                pre_order, in_order, in_s, lookup[node.value] - 1
            )
            node.right = _build_from_in_pre(
                pre_order, in_order, lookup[node.value] + 1, in_e
            )
        return node

    return _build_from_in_pre(pre_order, in_order, 0, len(in_order) - 1)


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        root = friendly_build(
            [
                ["7"],
                ["10", "2"],
                ["4", "3", "8", "N"],
                ["N", "N", "N", "1", "11", "N", "N", "N"],
            ]
        )

        pre_buf = []
        serialize_pre(root, pre_buf)

        in_buf = []
        serialize_in(root, in_buf)

        new_root = build_from_in_pre(pre_buf, in_buf)

        pretty_print(root)
        pretty_print(new_root)

        self.assertTrue(tree_equals(root, new_root))


if __name__ == "__main__":
    unittest.main()
