def weighted_edit_distance(n, m, s, t, I, D, S):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = i * D

    for j in range(1, m + 1):
        dp[0][j] = j * I

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + D,
                               dp[i][j - 1] + I,
                               dp[i - 1][j - 1] + S)

    return dp[n][m]


n, m = map(int, input().split())
s = input().strip()
t = input().strip()
I, D, S = map(int, input().split())

print(weighted_edit_distance(n, m, s, t, I, D, S))
