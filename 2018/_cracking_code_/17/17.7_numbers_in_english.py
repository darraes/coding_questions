from collections import deque

base_units = {
    "00": "zero",
    "01": "one",
    "02": "two",
    "03": "three",
    "04": "four",
    "05": "five",
    "06": "six",
    "07": "seven",
    "08": "eight",
    "09": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifthteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eightyteen",
    "19": "nineteen",
}

tens = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}

groups = ["", "thousand", "million", ]


def base_convert(number):
    if len(number) != 3:
        raise ValueError()

    res = ""

    if number[0] != "0":
        res += base_units["0" + number[0]] + " " + "hundred "
    if number[1] != "1" and number[1] != "0":
        res += tens[number[1]] + " "
    if number[1] != "0" or number[2] != "0":
        if number[1] != "1" and number[1] != "0":
            if number[2] != "0":
                res += base_units["0" + number[2]]
        elif number[1:] != "00":
            res += base_units[number[1:]]

    return res.strip()


def convert(number):
    parts = deque()
    while len(number) >= 3:
        part = number[len(number) - 3 :]
        parts.appendleft(part)
        number = number[: len(number) - 3]

    if len(number) > 0:
        part = number.zfill(3)
        parts.appendleft(part)

    res = ""
    i = len(parts) - 1
    j = 0
    while i >= 0:
        res = base_convert(parts[i]) + " " + groups[j] + " " + res
        i -= 1
        j += 1

    return res.strip()


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual("one hundred twenty three", convert("123"))
        self.assertEqual("four hundred", convert("400"))
        self.assertEqual("five hundred seventy", convert("570"))
        self.assertEqual("one", convert("1"))
        self.assertEqual("eleven", convert("11"))
        self.assertEqual("sixty one", convert("61"))
        self.assertEqual(
            "one million one thousand two hundred thirty four", convert("1001234")
        )


if __name__ == "__main__":
    unittest.main()
