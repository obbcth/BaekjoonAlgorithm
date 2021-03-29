n, s = list(map(int, input().split()))
nums = list(map(int, input().split()))
count = 0
visit = [0] * n

def backtracking(d, cur):
    global n, s, nums, count, visit

    if d == n:
        flag = 0
        for i in range(n):
            if visit[i] == 1:
                flag = 1

        if cur == s and flag == 1:
            count += 1
        return

    visit[d] = 1
    backtracking(d+1, cur+nums[d])
    visit[d] = 0
    backtracking(d+1, cur)

backtracking(0,0)
print(count)
