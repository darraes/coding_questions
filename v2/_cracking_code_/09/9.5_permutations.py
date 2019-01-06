def permutations(nums, idx = 0):
    if idx == len(nums):
        return [[]]

    ans = []
    sub_ans = permutations(nums, idx + 1)
    for sub in sub_ans:
        for i in range(len(sub) + 1):
            ans.append(sub[:i] + [nums[idx]] + sub[i:])
    return ans

print(permutations([1, 2, 3]))