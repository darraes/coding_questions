def url_encode(istr):
    chars = list(istr)

    spaces_count = 0
    for c in chars:
        if c == " ":
            spaces_count += 1

    chars += ["."] * 2 * spaces_count

    c = len(chars) - 1
    p = len(istr) - 1

    while p >= 0:
        if istr[p] == " ":
            chars[c] = "0"
            chars[c - 1] = "2"
            chars[c - 2] = "%"
            c -= 3
        else:
            chars[c] = istr[p]
            c -= 1

        p -= 1

    return "".join(chars)


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual("daniel%20arraes%20pereira", url_encode("daniel arraes pereira"))


if __name__ == '__main__':
    unittest.main()