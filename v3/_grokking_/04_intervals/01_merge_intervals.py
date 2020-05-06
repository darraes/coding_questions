from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")


def merge(intervals):
    merged = []

    intervals.sort(key=lambda i: i.start)
    current = None

    for interval in intervals:
        if not current:
            current = interval
        elif interval.start <= current.end:
            current.start = min(current.start, interval.start)
            current.end = max(current.end, interval.end)
        else:
            merged.append(current)
            current = interval

    if current:
        merged.append(current)

    return merged


def main():
    print("Merged intervals: ", end="")
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end="")
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end="")
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


main()
