def generate_generalized_abbreviation(word):
    def update_abbrev(abbrev, char):
        if len(abbrev) == 0 or char.isalpha() or abbrev[-1].isalpha():
            return abbrev + char
        return abbrev[:-1] + str(int(abbrev[-1]) + 1)

    result = [""]

    for char in word:
        cur_results = []
        for r in result:
            cur_results.append(update_abbrev(r, "1"))
            cur_results.append(update_abbrev(r, char))
        result = cur_results

    return result


def main():
    print(
        "Generalized abbreviation are: " + str(generate_generalized_abbreviation("BAT"))
    )
    print(
        "Generalized abbreviation are: "
        + str(generate_generalized_abbreviation("code"))
    )


main()
