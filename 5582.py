a = input()
b = input()

ans = 0

dp = [[0 for _ in range(4001)] for __ in range(4001)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans, dp[i][j])

print(ans)