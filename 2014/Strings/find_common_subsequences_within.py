# http://www.careercup.com/question?id=5931067269709824

def find_sub_sequences(str):
    first_occurence = dict()
    second_occurence = dict()

    for i in range(len(str)):
        if not first_occurence.has_key(str[i]): 
            first_occurence[str[i]] = i
        elif not second_occurence.has_key(str[i]): 
            second_occurence[str[i]] = i

    second = [(k, v) for k, v in second_occurence.iteritems()]
    for i in range(len(second)):
        for j in range(i + 1, len(second)):
            diff_sec = second[i][1] - second[j][1]
            diff_fir = first_occurence[second[i][0]] - first_occurence[second[j][0]]

            if diff_sec * diff_fir > 0: return True

    return False


print find_sub_sequences("abab")
print find_sub_sequences("abba")
print find_sub_sequences("acbdaghfb")
print find_sub_sequences("abcdacb")