def figure_out(solution, guess):
    frequency = {
        "R": 0,
        "G": 0,
        "B": 0,
        "Y": 0
    }

    hits = sub_hits = 0
    hits_idxs = set()
    for i in range(len(guess)):
        if guess[i] == solution[i]:
            hits += 1
            hits_idxs.add(i)
        else:
            frequency[solution[i]] += 1

    for i in range(len(guess)):
        if i not in hits_idxs and frequency[guess[i]] > 0:
            frequency[guess[i]] -= 1
            sub_hits += 1

    return hits, sub_hits


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual((3, 0), figure_out("RGBY", "RGBR"))
        self.assertEqual((2, 2), figure_out("RGBY", "RGYB"))
        self.assertEqual((0, 4), figure_out("RGBY", "YBRG"))


if __name__ == "__main__":
    unittest.main()