n, k = map(int, input().split())

dp = [[0 for __ in range(100001)] for _ in range(101)]
v = [0] + list(map(int, input().split()))

for x in range(1, k+1):
    dp[0][x] = 987654321

for i in range(1, n+1):
    for x in range(1, k+1):
        
        if x >= v[i]: # 더 마셔야 된다
            dp[i][x] = min(dp[i-1][x], dp[i-1][x-v[i]] + 1) # 이전에 마신거 +1
        else:
            dp[i][x] = dp[i-1][x]


if dp[n][k] == 987654321:
    print(-1)
else:
    print(dp[n][k])