from collections import defaultdict


class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        file_tracker = defaultdict(list)

        for entry in paths:
            parts = entry.split(" ")
            directory = parts[0]
            for file in parts[1:]:
                file_parts = file.split("(")

                file_name = file_parts[0]
                file_contents = file_parts[1][:-1]

                file_tracker[file_contents].append("{}/{}".format(directory, file_name))

        return [v for k, v in file_tracker.items() if len(v) > 1]


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertEqual(
            [],
            s.findDuplicate(
                [
                    "root/a 1.txt(abcd) 2.txt(efsfgh)",
                    "root/c 3.txt(abdfcd)",
                    "root/c/d 4.txt(efggdfh)",
                ]
            ),
        )

        self.assertEqual(
            [
                ["root/a/1.txt", "root/c/3.txt"],
                ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"],
            ],
            s.findDuplicate(
                [
                    "root/a 1.txt(abcd) 2.txt(efgh)",
                    "root/c 3.txt(abcd)",
                    "root/c/d 4.txt(efgh)",
                    "root 4.txt(efgh)",
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
