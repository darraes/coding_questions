def find_subsets(nums):
    subsets = []

    if len(nums) == 0:
        return [[]]

    me = nums[0]
    subs = find_subsets(nums[1:])

    subsets.extend(subs)
    for s in subs:
        subsets.append(s + [me])

    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
