def print_lines(X):
    for x in X:
        print(x)


#############################################
######### Longest Common Subsequence ########
#############################################


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


def lcs_length_rec(X, Y, m, n, cache):
    if m == len(X) or n == len(Y):
        return 0

    if (m, n) in cache:
        return cache[(m, n)]

    if X[m] == Y[n]:
        cache[(m, n)] = 1 + lcs_length_rec(X, Y, m + 1, n + 1, cache)
    else:
        cache[(m, n)] = max(
            lcs_length_rec(X, Y, m + 1, n, cache), lcs_length_rec(X, Y, m, n + 1, cache)
        )

    return cache[(m, n)]


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


def lcs_rec(X, Y, m, n, cache):
    if m == len(X) or n == len(Y):
        return []

    if (m, n) in cache:
        return cache[(m, n)]

    if X[m] == Y[n]:
        cache[(m, n)] = [X[m]] + lcs_rec(X, Y, m + 1, n + 1, cache)
    else:
        left = lcs_rec(X, Y, m + 1, n, cache)
        right = lcs_rec(X, Y, m, n + 1, cache)
        cache[(m, n)] = left if len(left) > len(right) else right

    return cache[(m, n)]


#############################################
######### Longest Common Substring ##########
#############################################


def lcsubstring_length(X, Y):
    m = len(X)
    n = len(Y)
    lookup = [[0 for y in range(len(Y) + 1)] for x in range(len(X) + 1)]

    max_len = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
                max_len = max(max_len, lookup[i][j])

    return max_len


def lcsubstring(X, Y):
    m = len(X)
    n = len(Y)
    lookup = [[0 for y in range(len(Y) + 1)] for x in range(len(X) + 1)]

    max_len = end_m = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
                if lookup[i][j] > max_len:
                    max_len = lookup[i][j]
                    end_m = i

    return X[end_m - max_len : end_m]


#############################################
######### Longest Palindromic Subsequence ###
#############################################


def lps_length_rec(X, i, j, cache):
    if i > j:
        return 0
    if i == j:
        return 1

    if (i, j) in cache:
        return cache[(i, j)]

    cost = 0
    if X[i] == X[j]:
        cost = 2

    cache[(i, j)] = max(
        cost + lps_length_rec(X, i + 1, j - 1, cache),
        lps_length_rec(X, i + 1, j, cache),
        lps_length_rec(X, i, j - 1, cache),
    )

    return cache[(i, j)]


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_lcs_length(self):
        self.assertEqual(4, lcs_length(list("ABCBDAB"), list("BDCABA"))[0])
        self.assertEqual(4, lcs_length_rec(list("ABCBDAB"), list("BDCABA"), 0, 0, {}))
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

        self.assertEqual(list("MJAU"), lcs_rec(X, Y, 0, 0, {}))

    def test_lcsubstring_length(self):
        self.assertEqual(4, lcsubstring_length("ABABC", "BABCA"))
        self.assertEqual(
            10,
            lcsubstring_length(
                "forgeeksskeegfor", "".join(reversed("forgeeksskeegfor"))
            ),
        )

    def test_lcsubstring(self):
        self.assertEqual("BABC", lcsubstring("ABABC", "BABCA"))

    def test_lps(self):
        s = "ABBDCACB"
        self.assertEqual(5, lps_length_rec(s, 0, len(s) - 1, {}))


if __name__ == "__main__":
    unittest.main()
