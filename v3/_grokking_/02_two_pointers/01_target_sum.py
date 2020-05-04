def pair_with_targetsum(arr, target_sum):
    begin = 0
    end = len(arr) - 1

    while end > begin:
        cur_sum = arr[begin] + arr[end]
        if cur_sum == target_sum:
            return [begin, end]
        elif cur_sum > target_sum:
            end -= 1
        else:
            begin += 1

    return [-1, -1]
