from collections import defaultdict
from queue import PriorityQueue


class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        heat_map = defaultdict(int)
        for task in tasks:
            heat_map[task] += 1

        queue = PriorityQueue()
        for task, count in heat_map.items():
            queue.put((-count, task))

        total_intervals = 0
        while not queue.empty():
            next_round = []
            processed = idle = 0
            for _ in range(n + 1):
                if not queue.empty():
                    processed += 1
                    count, task = queue.get()
                    if count < -1:
                        next_round.append((count + 1, task))
                else:
                    idle += 1

            for count, task in next_round:
                queue.put((count, task))

            total_intervals += processed
            if not queue.empty():
                total_intervals += idle

        return total_intervals


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertEqual(
            16,
            s.leastInterval(
                ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2
            ),
        )
        self.assertEqual(6, s.leastInterval(["A", "A", "A", "B", "B", "B"], 1))
        self.assertEqual(6, s.leastInterval(["A", "A", "A", "B", "B", "B"], 0))
        self.assertEqual(8, s.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
        self.assertEqual(10, s.leastInterval(["A", "A", "A", "B", "B", "B"], 3))
        self.assertEqual(9, s.leastInterval(["A", "A", "A", "B", "B", "C"], 3))


if __name__ == "__main__":
    unittest.main()
