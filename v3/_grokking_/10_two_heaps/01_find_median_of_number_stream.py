from heapq import heappush, heappop


class MedianOfAStream:
    def __init__(self):
        self.bottom = []
        self.top = []

    def insert_in_top(self, num):
        heappush(self.top, (num, num))

    def pop_from_top(self):
        _, num = heappop(self.top)
        return num

    def peek_top(self):
        return self.top[0][1]

    def insert_in_bottom(self, num):
        heappush(self.bottom, (-num, num))

    def pop_from_bottom(self):
        _, num = heappop(self.bottom)
        return num

    def peek_bottom(self):
        return self.bottom[0][1]

    def insert_num(self, num):
        if len(self.top) == 0:
            self.insert_in_top(num)
            return

        if self.peek_top() <= num:
            self.insert_in_top(num)
        else:
            self.insert_in_bottom(num)

        # rebalance
        if len(self.bottom) - len(self.top) >= 2:
            self.insert_in_top(self.pop_from_bottom())
        elif len(self.top) - len(self.bottom) >= 2:
            self.insert_in_bottom(self.pop_from_top())

        return

    def find_median(self):
        if len(self.top) == 0:
            return None
        if len(self.bottom) == 0:
            return self.peek_top()

        if len(self.top) == len(self.bottom):
            return (self.peek_bottom() + self.peek_top()) / 2
        elif len(self.top) > len(self.bottom):
            return self.peek_top()
        else:
            return self.peek_bottom()


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
