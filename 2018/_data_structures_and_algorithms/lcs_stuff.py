def print_lines(X):
    for x in X:
        print(x)


def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    lookup = [[0 for y in range(len(Y) + 1)] for x in range(len(X) + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
            else:
                lookup[i][j] = max(lookup[i][j - 1], lookup[i - 1][j])

    return lookup[m][n], lookup


def lcs(X, Y, m, n, lookup):
    if m == 0 or n == 0:
        return [[]]

    if X[m - 1] == Y[n - 1]:
        ans = lcs(X, Y, m - 1, n - 1, lookup)
        for s in ans:
            s.append(X[m - 1])

        return ans

    else:
        if lookup[m - 1][n] > lookup[m][n - 1]:
            return lcs(X, Y, m - 1, n, lookup)
        elif lookup[m][n - 1] > lookup[m - 1][n]:
            return lcs(X, Y, m, n - 1, lookup)

        ans = lcs(X, Y, m - 1, n, lookup)
        ans.extend(lcs(X, Y, m, n - 1, lookup))

        return ans


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_lcs_length(self):
        # self.assertEqual(4, lcs_length(list("ABCBDAB"), list("BDCABA"))[0])
        pass

    def test_lcs(self):
        X = list("ABCBDAB")
        Y = list("BDCABA")

        _, lookup = lcs_length(X, Y)
        self.assertEqual(
            [list("BCBA"), list("BCAB"), list("BDAB")],
            lcs(X, Y, len(X), len(Y), lookup),
        )

        X = list("XMJYAUZ")
        Y = list("MZJAWXU")

        _, lookup = lcs_length(X, Y)
        self.assertEqual([list("MJAU")], lcs(X, Y, len(X), len(Y), lookup))


if __name__ == "__main__":
    unittest.main()
