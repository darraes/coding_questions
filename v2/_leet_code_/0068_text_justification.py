class Line:
    def __init__(self):
        self.length = 0
        self.words = []

    def __str__(self):
        return " ".join(self.words)


class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lines = []
        cur_line = Line()
        for w in words:
            if cur_line.length + len(w) >= maxWidth and cur_line.length > 0:
                lines.append(cur_line)
                cur_line = Line()

            cur_line.length += len(w)
            cur_line.words.append(w)
            if len(w) < cur_line.length < maxWidth:
                cur_line.length += 1

        if cur_line.length > 0:
            lines.append(cur_line)

        def justify(words):
            s, r = left // (len(words) - 1), left % (len(words) - 1)
            line = ""
            for i in range(len(words)):
                line += words[i]
                if i < len(words) - 1:
                    line += "".join([" "] * (s + 1 if r > 0 else s))
                    r -= 1
            return line

        def left_align(words):
            nonlocal maxWidth
            line = ""
            for i in range(len(words)):
                line += words[i]
                if i < len(words) - 1:
                    line += " "
            line += "".join([" "] * (maxWidth - len(line)))
            return line

        res = []
        for i in range(len(lines)):
            left = maxWidth - sum([len(w) for w in lines[i].words])
            if len(lines[i].words) > 1 and i < len(lines) - 1:
                res.append(justify(lines[i].words))
            else:
                res.append(left_align(lines[i].words))

        return res


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            ["Listen", "to    ", "many, ", "speak ", "to   a", "few.  "],
            s.fullJustify(["Listen", "to", "many,", "speak", "to", "a", "few."], 6),
        )

        self.assertEqual(
            [
                "Science  is  what we",
                "understand      well",
                "enough to explain to",
                "a  computer.  Art is",
                "everything  else  we",
                "do                  ",
            ],
            s.fullJustify(
                [
                    "Science",
                    "is",
                    "what",
                    "we",
                    "understand",
                    "well",
                    "enough",
                    "to",
                    "explain",
                    "to",
                    "a",
                    "computer.",
                    "Art",
                    "is",
                    "everything",
                    "else",
                    "we",
                    "do",
                ],
                20,
            ),
        )

        self.assertEqual(
            ["This    is    an", "example  of text", "justification.  "],
            s.fullJustify(
                ["This", "is", "an", "example", "of", "text", "justification."], 16
            ),
        )

        self.assertEqual(
            ["What   must   be", "acknowledgment  ", "shall be        "],
            s.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16),
        )


if __name__ == "__main__":
    unittest.main()
