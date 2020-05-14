def find_subsets(nums):
    subsets = [[]]
    previous_round, last = [[]], None

    nums.sort()

    for n in nums:
        new_subsets = []

        to_use = subsets if n != last else previous_round
        for s in to_use:
            new_subsets.append(s + [n])
        subsets.extend(new_subsets)

        previous_round = new_subsets
        last = n
    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
