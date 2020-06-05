def can_partition(nums):
    s = sum(nums)

    if s % 2 == 1:
        return False

    return has_subset(nums, s // 2, 0, 0, {})


def has_subset(nums, s, cur_s, idx, dp):
    if idx == len(nums):
        return False

    if cur_s + nums[idx] == s:
        return True

    if (cur_s, idx) not in dp:
        tmp_result = has_subset(nums, s, cur_s, idx + 1, dp)
        if not tmp_result and cur_s + nums[idx] < s:
            tmp_result |= has_subset(nums, s, cur_s + nums[idx], idx + 1, dp)

        dp[(cur_s, idx)] = tmp_result

    return dp[(cur_s, idx)]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
