def move_disks(n, tower1, tower2, tower3):
    if n == 0:
        print("T1", tower1)
        print("T2", tower2)
        print("T3", tower3)
        return

    move_disks(n - 1, tower1, tower3, tower2)
    tower2.append(tower1.pop())
    move_disks(n - 1, tower3, tower2, tower1)



###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        tower = [5, 4, 3, 2, 1]
        dst = []

        move_disks(5, tower, dst, [])

if __name__ == "__main__":
    unittest.main()
