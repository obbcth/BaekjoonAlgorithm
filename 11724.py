import sys
sys.setrecursionlimit(10000)

n, m = list(map(int, input().split()))

vec = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = list(map(int, input().split()))
    vec [a][b] = True
    vec [b][a] = True

visit = [0] * (n+1)

def dfs(v):
    visit[v] = 1

    for i in range(1, n + 1):
        if visit[i] == 0 and vec[v][i] == 1:
            dfs(i)

count = 0

for i in range(1, n + 1):
    if visit[i] == 0:
        dfs(i)
        count += 1

print(count)
