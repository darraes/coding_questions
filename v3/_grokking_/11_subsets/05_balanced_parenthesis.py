def generate_valid_parentheses(num):
    if num == 0:
        return [""]
    if num == 1:
        return ["()"]

    result = set()
    for p in generate_valid_parentheses(num - 1):
        for i in range(len(p) + 1):
            result.add(p[:i] + "()" + p[i:])

    return result


def main():
    print(
        "All combinations of balanced parentheses are: "
        + str(generate_valid_parentheses(2))
    )
    print(
        "All combinations of balanced parentheses are: "
        + str(generate_valid_parentheses(3))
    )


main()
