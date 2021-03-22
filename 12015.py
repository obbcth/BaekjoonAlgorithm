from bisect import bisect_left

n = int(input())

nums = list(map(int, input().split()))

dp = [0, ]

for i in nums:
    t = bisect_left(dp, i)
    
    if len(dp) <= t:
        dp.append(i)
    else:
        dp[t] = i

print(len(dp)-1)
