from math import sqrt
from heapq import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "]\n", end="")


def find_closest_points(points, k):
    result = []

    for i in range(k):
        d = points[i].distance()
        heappush(result, (-d, points[i]))

    for i in range(k, len(points)):
        d = points[i].distance()
        if -d > result[0][0]:
            heappop(result)
            heappush(result, (-d, points[i]))

    return [r[1] for r in result]


def main():
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ")
    for point in result:
        point.print_point()


main()
