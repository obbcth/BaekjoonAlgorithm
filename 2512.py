n = int(input())

nums = list(map(int, input().split()))
total = int(input())

low = 0
high = max(nums)

while low <= high:
    mid = (low + high) // 2
    sum = 0
    for i in nums:
        if i >= mid:
            sum += mid
        else:
            sum += i
    if sum <= total:
        low = mid + 1
    else:
        high = mid - 1

print(high)
