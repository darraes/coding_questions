def m_in_n(N, M, i, j):
    # 1 - create a mask to 0 bits i to j in N
    #   1.1 - Right side of mask - all bits after j set to 1, rest 0
    #   1.2 - Left side of mask - all bits before i set to 1, rest 0
    #   1.3 - Merge above sub-masks
    # 2 - N & mask will 0 digits i to j on N
    # 3 - Shift M j positions to the left
    # 4 - return N & M

    left = ~0
    left = left << (i + 1)

    right = (1 << j) - 1

    mask = left | right

    N = N & mask
    M = M << j

    return N | M


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        # 10000000000       
        # 00000000101
        # 10000010100
        self.assertEqual(1044, m_in_n(1024, 5, 4, 2))

        # 10000000000       
        # 00000000101
        # 10001010000
        self.assertEqual(1104, m_in_n(1024, 5, 6, 4))


if __name__ == '__main__':
    unittest.main()