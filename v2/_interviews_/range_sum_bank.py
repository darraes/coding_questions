"""
Implementation for a bank account api that supports the following operations:

credit(timestamp, amount) # O(1)

debit(timestamp, amount) # O(1)

current() # current balance but with O(1) operation

balance(exclusive_start_timestamp, inclusive_end_timestamp) # O(log M) M being the number of items

For the sake of the exercise, all parameters can just be ints

The timestamps will appear in sorted order.

Example:

5 credit $5
7 credit $10
10 debit $3
12 debit $2
14 debit $1

current() == $9

balance(7, 12) == -$5
balance(10, 14) == -$3
balance(11, 22) == -$3
balance(4, 50) == $9
balance(5, 7) == $10
"""

from bisect import bisect_left, bisect_right


class BankAccount:
    def __init__(self):
        self._current = [(0, 0)]  # (timestamp, balance)

    def credit(self, timestamp, amount):
        b = self.current()
        self._current.append((timestamp, b + amount))

    def debit(self, timestamp, amount):
        self.credit(timestamp, -amount)

    def current(self):
        _, b = self._current[-1]
        return b

    def balance(self, start, end):
        s_idx = min(bisect_right(self._current, (start, 0)), len(self._current) - 1)
        e_idx = min(bisect_right(self._current, (end, 0)), len(self._current) - 1)

        if self._current[s_idx][0] > start:
            s_idx = max(0, s_idx - 1)

        if self._current[e_idx][0] > end:
            e_idx = max(0, e_idx - 1)

        return self._current[e_idx][1] - self._current[s_idx][1]


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        account = BankAccount()

        account.credit(5, 5)
        account.credit(7, 10)
        account.debit(10, 3)
        account.debit(12, 2)
        account.debit(14, 1)
        self.assertEqual(9, account.current())

        self.assertEqual(-5, account.balance(8, 12))
        self.assertEqual(-3, account.balance(7, 11))

        self.assertEqual(0, account.balance(15, 20))
        self.assertEqual(0, account.balance(2, 4))
        self.assertEqual(5, account.balance(4, 6))
        self.assertEqual(9, account.balance(4, 50))
        self.assertEqual(-3, account.balance(11, 22))
        self.assertEqual(-5, account.balance(7, 12))
        self.assertEqual(-3, account.balance(10, 14))
        self.assertEqual(10, account.balance(5, 7))


if __name__ == "__main__":
    unittest.main()
