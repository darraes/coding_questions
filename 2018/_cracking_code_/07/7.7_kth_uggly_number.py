from collections import deque

def kth_uggly_number(k):
    q3 = deque([3])
    q5 = deque([5])
    q7 = deque([7])

    n = 1
    res = 0
    while n <= k:
        nth_number = min(q3[0], q5[0], q7[0])

        if nth_number == q3[0]:
            res = q3.popleft()
            q3.append(3 * nth_number)
            q5.append(5 * nth_number)
            q7.append(7 * nth_number)
        elif nth_number == q5[0]:
            res = q5.popleft()
            q5.append(5 * nth_number)
            q7.append(7 * nth_number)
        else:
            res = q7.popleft()
            q7.append(7 * nth_number)

        n += 1

    return res



###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, kth_uggly_number(1))
        self.assertEqual(5, kth_uggly_number(2))
        self.assertEqual(7, kth_uggly_number(3))
        self.assertEqual(9, kth_uggly_number(4))
        self.assertEqual(15, kth_uggly_number(5))
        self.assertEqual(21, kth_uggly_number(6))
        self.assertEqual(25, kth_uggly_number(7))
        self.assertEqual(27, kth_uggly_number(8))
        self.assertEqual(35, kth_uggly_number(9))


if __name__ == '__main__':
    unittest.main()