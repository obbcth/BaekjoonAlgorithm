import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
case = int(input())

dp = [[0]*n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1
    else:
        dp[i][i+1] = 0

for idx in range(n-2):
    for i in range(n-2-idx):
        j = i + 2 + idx

        if arr[i] == arr[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1

for _ in range(case):
    start, end = map(int, input().split())
    print(dp[start-1][end-1])
