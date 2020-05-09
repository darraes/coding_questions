def longest_substring_with_k_distinct(str, k):
  window = {}
  
  def add_to_window(char):
      nonlocal window
      if char not in window:
          window[char] = 0
      window[char] += 1

  def del_from_window(char):
      nonlocal window
      window[char] -= 1
      if window[char] == 0:
          del window[char]

  max_length = window_start = 0

  for window_end in range(len(str)):
      add_to_window(str[window_end])

      while len(window) > k:
          del_from_window(str[window_start])
          window_start += 1

      max_length = max(max_length, window_end - window_start + 1)

  return max_length

###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(4, longest_substring_with_k_distinct("araaci", 2))
        self.assertEqual(2, longest_substring_with_k_distinct("araaci", 1))
        self.assertEqual(5, longest_substring_with_k_distinct("cbbebi", 3))


if __name__ == "__main__":
    unittest.main()