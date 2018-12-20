def print_lines(X):
    for x in X:
        print(x)


def levenshtein_distance_rec(X, m, Y, n, cache):
    if m == len(X):
        return len(Y) - n
    if n == len(Y):
        return len(X) - m

    if (m, n) in cache:
        return cache[(m, n)]

    cost = 1
    if X[m] == Y[n]:
        cost = 0

    cache[(m, n)] = min(
        levenshtein_distance_rec(X, m + 1, Y, n + 1, cache) + cost,
        levenshtein_distance_rec(X, m, Y, n + 1, cache) + 1,
        levenshtein_distance_rec(X, m + 1, Y, n, cache) + 1,
    )

    return cache[(m, n)]


def levenshtein_distance(X, Y):
    m = len(X)
    n = len(Y)
    lookup = [[0 for y in range(len(Y) + 1)] for x in range(len(X) + 1)]

    for i in range(m + 1):
        lookup[i][0] = i

    for j in range(n + 1):
        lookup[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 1
            if X[i - 1] == Y[j - 1]:
                cost = 0

            lookup[i][j] = min(
                lookup[i - 1][j - 1] + cost, lookup[i - 1][j] + 1, lookup[i][j - 1] + 1
            )

    return lookup[m][n]


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, levenshtein_distance_rec("kitten", 0, "sitting", 0, {}))
        self.assertEqual(3, levenshtein_distance("sitting", "kitten"))


if __name__ == "__main__":
    unittest.main()
