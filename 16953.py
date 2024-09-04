a, b = map(int, input().split())
answer = []

def dfs(th, idx):
    m = th * 2
    n = th * 10 + 1

    if m == b:
        answer.append(idx+1)
    
    if m < b:
        dfs(m, idx+1)

    if n == b:
        answer.append(idx+1)
    
    if n < b:
        dfs(n, idx+1)

dfs(a, 1)

if len(answer) != 0:
    print(min(answer))
else:
    print(-1)