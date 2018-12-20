def one_edit(str1, str2):
    diff = 0
    if (len(str1) == len(str2)):
        for i in range(len(str1)):
            if str1[i] != str2[i]: diff += 1
            if diff > 1: return False
        return True
    else:
        big = str1
        small = str2
        if (len(big) < len(small)): 
            small = str1
            big = str2

        i = 0
        j = 0

        while(i < len(big)):
            if j == len(str2) - 1: return True

            if big[i] == small[j]:
                i += 1
                j += 1
            else:
                i += 1
                diff += 1
                if (diff >= 2): return False

    return True



print one_edit("wrtyu", "wrtyu")