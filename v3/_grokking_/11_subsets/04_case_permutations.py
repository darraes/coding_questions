def find_letter_case_string_permutations(str):
    permutations = [""]

    for char in str:
        new_perms = []
        for p in permutations:
            new_perms.append(p + char)
            if char.isalpha():
                new_perms.append(p + char.swapcase())
        permutations = new_perms

    return permutations


def main():
    print(
        "String permutations are: " + str(find_letter_case_string_permutations("ad52"))
    )
    print(
        "String permutations are: " + str(find_letter_case_string_permutations("ab7c"))
    )


main()
