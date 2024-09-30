n, k = map(int, input().split())

dp = [[0 for __ in range(100001)] for _ in range(101)]
w = [0]
v = [0]

for _ in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

for i in range(1, n+1):
    for x in range(1, k+1):
        dp[i][x] = dp[i-1][x]
        if x >= w[i]:
            dp[i][x] = max(dp[i][x], dp[i-1][x-w[i]] + v[i])

print(dp[n][k])