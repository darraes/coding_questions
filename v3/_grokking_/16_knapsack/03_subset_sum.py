def can_partition(nums, s):
    return can_partition_impl({}, nums, s, 0, 0)


def can_partition_impl(dp, nums, s, idx, cur_s):
    if idx >= len(nums):
        return False

    if cur_s + nums[idx] == s:
        return True

    if (idx, cur_s) not in dp:
        result = can_partition_impl(dp, nums, s, idx + 1, cur_s)

        if cur_s + nums[idx] < s:
            result |= can_partition_impl(dp, nums, s, idx + 1, cur_s + nums[idx])

        dp[(idx, cur_s)] = result
    return dp[(idx, cur_s)]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
