from heapq import heappush, heappop, heapify


class MedianCalculator:
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

    def maybe_rebalance(self):
        if len(self.bottom) - len(self.top) >= 2:
            self.insert_in_top(self.pop_from_bottom())
        elif len(self.top) - len(self.bottom) >= 2:
            self.insert_in_bottom(self.pop_from_top())

    def insert_num(self, num):
        if len(self.top) == 0:
            self.insert_in_top(num)
            return

        if self.peek_top() <= num:
            self.insert_in_top(num)
        else:
            self.insert_in_bottom(num)

        self.maybe_rebalance()
        return

    def remove_num(self, num):
        def remove(heap, element):
            ind = heap.index(element)
            heap[ind] = heap[-1]
            del heap[-1]
            heapify(heap)

        if self.peek_top() <= num:
            remove(self.top, (num, num))
        else:
            remove(self.bottom, (-num, num))

        self.maybe_rebalance()
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


class SlidingWindowMedian:
    def find_sliding_window_median(self, nums, k):
        calc = MedianCalculator()
        result = []
        left = 0
        for right in range(len(nums)):
            if right < k:
                calc.insert_num(nums[right])
                continue

            result.append(calc.find_median())
            calc.insert_num(nums[right])
            calc.remove_num(nums[left])
            left += 1
        
        result.append(calc.find_median())
        return result


def main():

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
