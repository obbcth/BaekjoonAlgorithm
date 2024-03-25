# n, m, v = list(map(int, input().split()))
n, k = list(map(int, input().split()))

visit = [-1] * (101010)

def bfs(v):
    queue = [v]
    visit[v] = 0

    while queue:
        v = queue[0]
        del queue[0]

        # 현재 좌표를 딱 때리다
        if v*2 <= k+1 and visit[v*2] == -1:
            visit[v*2] = visit[v] + 1
            queue.append(v*2)
            
        if v-1 >= 0 and visit[v-1] == -1:
            visit[v-1] = visit[v] + 1
            queue.append(v-1)
            
        if v+1 <= k+1 and visit[v+1] == -1:
            visit[v+1] = visit[v] + 1
            queue.append(v+1)

    return visit[k]
            
print(bfs(n))

