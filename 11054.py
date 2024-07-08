n = int(input())
arr = list(map(int, input().split()))

answer = 0

dp = [[0] * n, [0] * n]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[0][i] = max(dp[0][i], dp[0][j])
        elif arr[i] < arr[j]:
            dp[1][i] = max(dp[1][i], dp[0][j], dp[1][j])
    dp[0][i] += 1
    dp[1][i] += 1
    answer = max(answer, dp[0][i], dp[1][i])

print(answer)
