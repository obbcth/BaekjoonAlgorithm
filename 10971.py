n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

visited = [0] * n
costsum = 0
ans = 987654321

def dfs(idx, idxbefor):
    global costsum, ans

    if idx == n-1:
        if cost[idxbefor][0]:
            costsum += cost[idxbefor][0]
            ans = min(ans, costsum)
            costsum -= cost[idxbefor][0]
        return
    
    for i in range(1, n):
        if not visited[i] and cost[idxbefor][i]:
            visited[i] = 1
            costsum += cost[idxbefor][i]
            dfs(idx+1, i)
            visited[i] = 0
            costsum -= cost[idxbefor][i]
    return

dfs(0, 0)
print(ans)