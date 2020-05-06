def insert(intervals, new_interval):
    start, end = 0, 1
    merged = []

    i = 0
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1

    merged.append(new_interval)

    while i < len(intervals):
        if intervals[i][start] <= merged[-1][end]:
            merged[-1][end] = max(merged[-1][end], intervals[i][end])
            merged[-1][start] = min(merged[-1][start], intervals[i][start])
        else:
            merged.append(intervals[i])
        i += 1

    return merged


def main():
    print(
        "Intervals after inserting the new interval: "
        + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6]))
    )
    print(
        "Intervals after inserting the new interval: "
        + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10]))
    )
    print(
        "Intervals after inserting the new interval: "
        + str(insert([[2, 3], [5, 7]], [1, 4]))
    )


main()
