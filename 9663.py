
n = int(input())
cnt = 0

arr = [0] * 15
ch1 = [0] * 44
ch2 = [0] * 44

def check(idx, y):
    return arr[y] or ch1[y-idx+n] or ch2[y+idx]

def dfs(idx):
    global cnt
    
    if (idx == n):
        cnt += 1
        return

    for i in range(n):
        if not check(idx, i):
            arr[i] = 1
            ch1[i - idx + n] = 1
            ch2[i + idx] = 1

            dfs(idx+1)

            arr[i] = 0
            ch1[i - idx + n] = 0
            ch2[i + idx] = 0
    return

dfs(0)
print(cnt)
            