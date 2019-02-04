class Solution:
    def largestRectangleArea(self, histogram):
        # This function calulates maximum
        # rectangular area under given
        # histogram with n bars

        # Create an empty stack. The stack
        # holds indexes of histogram[] list.
        # The bars stored in the stack are
        # always in increasing order of
        # their heights.
        stack = list()

        max_area = 0  # Initalize max area

        # Run through all bars of
        # given histogram
        index = 0
        while index < len(histogram):
            # If this bar is higher
            # than the bar on top
            # stack, push it to stack

            if (not stack) or (histogram[stack[-1]] <= histogram[index]):
                stack.append(index)
                index += 1

            # If this bar is lower than top of stack,
            # then calculate area of rectangle with
            # stack top as the smallest (or minimum
            # height) bar.'i' is 'right index' for
            # the top and element before top in stack
            # is 'left index'
            else:
                # pop the top
                top_of_stack = stack.pop()

                # Calculate the area with
                # histogram[top_of_stack] stack
                # as smallest bar
                area = histogram[top_of_stack] * (
                    (index - stack[-1] - 1) if stack else index
                )

                # update max area, if needed
                max_area = max(max_area, area)

        # Now pop the remaining bars from
        # stack and calculate area with
        # every popped bar as the smallest bar
        while stack:
            # pop the top
            top_of_stack = stack.pop()

            # Calculate the area with
            # histogram[top_of_stack]
            # stack as smallest bar
            area = histogram[top_of_stack] * (
                (index - stack[-1] - 1) if stack else index
            )

            # update max area, if needed
            max_area = max(max_area, area)

        # Return maximum area under
        # the given histogram
        return max_area

    def largestRectangleAreaDC(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        def restricted_largest(heights, i, j):
            if i > j:
                return 0
            if i == j:
                return heights[i]

            cur_min = cur_min_idx = -1
            for idx in range(i, j + 1):
                if cur_min == -1 or heights[idx] < cur_min:
                    cur_min = heights[idx]
                    cur_min_idx = idx

            return max(
                cur_min * (j - i + 1),
                restricted_largest(heights, i, cur_min_idx - 1),
                restricted_largest(heights, cur_min_idx + 1, j),
            )

        return restricted_largest(heights, 0, len(heights) - 1)


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(10, s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
        self.assertEqual(3, s.largestRectangleArea([3]))
        self.assertEqual(8, s.largestRectangleArea([2, 1, 5, 2, 2, 3]))
        self.assertEqual(30, s.largestRectangleArea([10, 10, 10, 9]))


if __name__ == "__main__":
    unittest.main()
