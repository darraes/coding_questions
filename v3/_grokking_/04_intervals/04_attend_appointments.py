def can_attend_all_appointments(intervals):
    start, end = 0, 1
    intervals.sort(key=lambda i: i[start])

    for i in range(1, len(intervals)):
        if intervals[i - 1][end] >= intervals[i][start]:
            return False

    return True


def main():
    print(
        "Can attend all appointments: "
        + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]]))
    )
    print(
        "Can attend all appointments: "
        + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]]))
    )
    print(
        "Can attend all appointments: "
        + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]]))
    )


main()
