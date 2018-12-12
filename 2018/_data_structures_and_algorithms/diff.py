def print_lines(X):
    for x in X:
        print(x)


def lcs_lookup(X, Y):
    m = len(X)
    n = len(Y)
    lookup = [[0 for y in range(len(Y) + 1)] for x in range(len(X) + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
            else:
                lookup[i][j] = max(lookup[i][j - 1], lookup[i - 1][j])

    return lookup


def diff(X, Y, m, n, lookup, res):
    if m > 0 and n > 0 and X[m - 1] == Y[n - 1]:
        diff(X, Y, m - 1, n - 1, lookup, res)
        res.append(X[m - 1])
    elif n > 0 and (m == 0 or lookup[m][n - 1] >= lookup[m - 1][n]):
        diff(X, Y, m, n - 1, lookup, res)
        res.append("+" + Y[n - 1])
    elif m > 0 and (n == 0 or lookup[m - 1][n] > lookup[m][n - 1]):
        diff(X, Y, m - 1, n, lookup, res)
        res.append("-" + X[m - 1])


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_diff(self):
        X = "ABCDFGHJQZ"
        Y = "ABCDEFGIJKRXYZ"
        res = []
        diff(X, Y, len(X), len(Y), lcs_lookup(X, Y), res)
        self.assertEqual("A B C D +E F G -H +I J -Q +K +R +X +Y Z", " ".join(res))

        X = "XMJYAUZ"
        Y = "XMJAATZ"
        res = []
        diff(X, Y, len(X), len(Y), lcs_lookup(X, Y), res)
        self.assertEqual("A B C D +E F G -H +I J -Q +K +R +X +Y Z", " ".join(res))


if __name__ == "__main__":
    unittest.main()
