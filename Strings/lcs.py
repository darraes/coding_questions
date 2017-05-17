def lcs_length(strA, strB):
    L = [[0 for y in range(len(strB) + 1)] for x in range(len(strA) + 1)]

    for i in reversed(range(len(strA))):
        for j in reversed(range(len(strB))):
            if (strA[i] == strB[j]): 
                L[i][j] = L[i + 1][j + 1] + 1
            else: 
                L[i][j] = max(L[i + 1][j], L[i][j + 1])

    return L[0][0];



print lcs_length("daniel", "dnel")

    
    