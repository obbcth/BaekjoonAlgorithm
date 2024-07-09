n = int(input())
dp = [[0, 0, 0]]

for idx in range(1, n+1):
    r, g, b = map(int, input().split())
    dp.append( [ min(r + dp[idx-1][1], r + dp[idx-1][2]) , min(g + dp[idx-1][0], g + dp[idx-1][2]) , min(b + dp[idx-1][0], b + dp[idx-1][1]) ] )

print(min(dp[n]))