def find_permutations(nums):
    result = [[]]

    for n in nums:
        next_result = []

        for r in result:
            for i in range(len(r) + 1):
                next_result.append(r[:i] + [n] + r[i:])

        result = next_result

    return result


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
