n, m, v = list(map(int, input().split()))

vec = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = list(map(int, input().split()))
    vec [a][b] = True
    vec [b][a] = True

visit = [0] * (n+1)

def dfs(v):
    print(v, end=' ')
    visit[v] = 1

    for i in range(1, n + 1):
        if visit[i] == 0 and vec[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = [v]
    visit[v] = 0

    while queue:
        v = queue[0]
        print(v, end=' ')
        del queue[0]

        for i in range(1, n+1):
            if visit[i] == 1 and vec[v][i] == 1:
                queue.append(i)
                visit[i] = 0

dfs(v)
print()
bfs(v)
