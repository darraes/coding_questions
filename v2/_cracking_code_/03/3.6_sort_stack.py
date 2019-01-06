def sort_stack(stack):
    if len(stack) == 0:
        return

    element = stack.pop()
    sort_stack(stack)

    buf = []
    while len(stack) > 0 and stack[-1] < element:
        buf.append(stack.pop())

    stack.append(element)
    for _ in range(len(buf)):
        stack.append(buf.pop())

    return stack


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        problem = [2, 4, 6, 1, 8, 7, 9]
        sort_stack(problem)
        self.assertEqual(sorted([2, 4, 6, 1, 8, 7, 9], reverse=True), problem)


if __name__ == "__main__":
    unittest.main()
