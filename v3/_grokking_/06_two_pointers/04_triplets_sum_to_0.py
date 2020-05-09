def search_triplets(arr):
    triplets = []

    arr = sorted(arr)

    for x in range(len(arr) - 2):
        y, z = x + 1, len(arr) - 1
        while y < z:
            if arr[x] + arr[y] + arr[z] == 0:
                triplets.append([arr[x], arr[y], arr[z]])

            if arr[x] + arr[y] + arr[z] > 0:
                z_value = arr[z]
                while z_value == arr[z] and y < z:
                    z -= 1
            else:
                y_value = arr[y]
                while y_value == arr[y] and y < z:
                    y += 1

    return triplets


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]],
            search_triplets([-3, 0, 1, 2, -1, 1, -2]),
        )
        self.assertEqual(
            [[-5, 2, 3], [-2, -1, 3]],
            search_triplets([-5, 2, -1, -2, 3]),
        )


if __name__ == "__main__":
    unittest.main()
