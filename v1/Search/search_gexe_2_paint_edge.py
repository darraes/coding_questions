# https://code.google.com/p/prep/wiki/ExercisesList

# Implement edge fill (four-way): suppose each number represents a color, suppose the currently
# selected color is 2 (the color that will be painted), and suppose you click on the X (whose value is also 0)
# on the picture on the left. Your algorithm should end up with the picture on the right
# (as a follow up, do it in N dimensions):

# 111111111                       111111111
# 111111111                       112222211
# 110000011                       120000021
# 1100x0011          ==>          120000021
# 110000011                       120000021
# 111111111                       112222211
# 111111111                       111111111


from collections import deque


def adjacents(matrix, x, y):
    return [
        point
        for point in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        if point[0] >= 0
        and point[0] < len(matrix)
        and point[1] >= 0
        and point[1] < len(matrix[0])
    ]


def paint_edge(image, color, click):
    click_color = image[click[0]][click[1]]

    if color == click_color:
        return

    queue = deque()
    visited = set()
    queue.append(click)

    while len(queue) > 0:
        current = queue.popleft()
        visited.add(current)

        if image[current[0]][current[1]] != click_color:
            image[current[0]][current[1]] = color
            continue
        else:
            for p in [
                p for p in adjacents(image, current[0], current[1]) if p not in visited
            ]:
                queue.append(p)
    return


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_simple_fill(self):
        image = [
            [0, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

        result = [
            [0, 0, 1, 0, 2, 2],
            [1, 0, 1, 2, 1, 1],
            [1, 1, 1, 2, 1, 1],
            [0, 0, 0, 0, 2, 2],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

        paint_edge(image, 2, (1, 4))
        self.assertEqual(result, image)

    def test_simple_fill_2(self):
        image = [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 1],
            [0, 1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

        result = [
            [0, 2, 2, 0, 0, 0],
            [2, 1, 1, 2, 1, 1],
            [2, 1, 1, 2, 1, 1],
            [0, 2, 2, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

        paint_edge(image, 2, (1, 1))
        self.assertEqual(result, image)


if __name__ == "__main__":
    unittest.main()
