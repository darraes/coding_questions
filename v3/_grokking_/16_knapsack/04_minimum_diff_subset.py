def can_partition(nums):
    return min_difference_impl({}, nums, 0, 0, 0)

def min_difference_impl(dp, nums, idx, l_sum, r_sum):
    if idx == len(nums):
        return abs(l_sum - r_sum)

    if (idx, l_sum) not in dp:
        dp[(idx, l_sum)] = min(
            min_difference_impl(dp, nums, idx + 1, l_sum + nums[idx], r_sum),
            min_difference_impl(dp, nums, idx + 1, l_sum, r_sum + nums[idx]),
        )

    return dp[(idx, l_sum)]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
