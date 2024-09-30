a = input()
b = input()

dp = [[0 for _ in range(1001)] for __ in range(1001)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

print(dp[len(a)][len(b)])