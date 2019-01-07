from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        connections = defaultdict(list)
        for ticket in sorted(tickets)[::-1]:
            connections[ticket[0]].append((ticket[1]))

        route = []
        def itinerary(start):
            while connections[start]:
                itinerary(connections[start].pop())
            route.append(start)
            
        itinerary("JFK")
        return route[::-1]


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertEqual(
            ['JFK', 'NRT', 'JFK', 'KUL'],
            s.findItinerary(
                [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
            ),
        )

        return

        self.assertEqual(
            [
                "JFK",
                "ANU",
                "EZE",
                "AXA",
                "TIA",
                "ANU",
                "JFK",
                "TIA",
                "ANU",
                "TIA",
                "JFK",
            ],
            s.findItinerary(
                [
                    ["EZE", "AXA"],
                    ["TIA", "ANU"],
                    ["ANU", "JFK"],
                    ["JFK", "ANU"],
                    ["ANU", "EZE"],
                    ["TIA", "ANU"],
                    ["AXA", "TIA"],
                    ["TIA", "JFK"],
                    ["ANU", "TIA"],
                    ["JFK", "TIA"],
                ]
            ),
        )

        self.assertEqual(
            ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
            s.findItinerary(
                [
                    ["JFK", "SFO"],
                    ["JFK", "ATL"],
                    ["SFO", "ATL"],
                    ["ATL", "JFK"],
                    ["ATL", "SFO"],
                ]
            ),
        )

        self.assertEqual(
            ["JFK", "MUC", "LHR", "SFO", "SJC"],
            s.findItinerary(
                [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
            ),
        )


if __name__ == "__main__":
    unittest.main()
