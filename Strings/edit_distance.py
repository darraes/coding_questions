def distance(phrase, k):
    rphrase = phrase[::-1]
    l = len(phrase)
    dp = [[0 for x in xrange(l)] for x in xrange(l)] 
    for i in range(l):
        dp[i][0] = dp[0][i] = i;

    for i in range(1, l):
        for j in range(1, l):
            if phrase[i] == rphrase[j]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                 dp[i][j] = min(dp[i][j - 1] + 1
                                , dp[i - 1][j] + 1
                                , dp[i-1][j-1] + 1)

    return dp[l - 1][l - 1]