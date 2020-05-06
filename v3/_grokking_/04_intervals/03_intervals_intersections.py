from collections import deque


def merge(intervals_a, intervals_b):
    result = []
    starts = []
    ends = []

    for i in intervals_a:
        starts.append(i[0])
        ends.append(i[1])

    for i in intervals_b:
        starts.append(i[0])
        ends.append(i[1])

    starts.sort()
    ends.sort()

    starts = deque(starts)
    ends = deque(ends)

    intersecting = 0
    inter_start = -1
    while len(starts) > 0 or len(ends) > 0:
        if len(starts) > 0 and len(ends) > 0 and starts[0] <= ends[0]:
            intersecting += 1
            start = starts.popleft()
            if intersecting == 2:
                result.append([start, ends.popleft()])
                intersecting -= 1
        else:
            ends.popleft()
            intersecting -= 1

    return result


def main():
    print(
        "Intervals Intersection: "
        + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]))
    )
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
