import heapq

n, e = map(int, input().split())

edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append([a, b, c])

v1, v2 = map(int, input().split())

def djikstra(idx):
    visited[idx] = 1
    visit_list = []
    for edge in edges:
        if edge[0] == idx:

            if dp[edge[1]] > dp[edge[0]] + edge[2]:
                 dp[edge[1]] = dp[edge[0]] + edge[2]

            if visited[edge[1]] == 0:
                heapq.heappush(visit_list, (dp[edge[1]], edge[1]))

        if edge[1] == idx:

            if dp[edge[0]] > dp[edge[1]] + edge[2]:
                 dp[edge[0]] = dp[edge[1]] + edge[2]

            if visited[edge[0]] == 0:
                heapq.heappush(visit_list, (dp[edge[0]], edge[0]))
    
    if len(visit_list) > 0:
        next = heapq.heappop(visit_list)
        return djikstra(next[1])

    return dp

# 1부터 n까지 이동하는데, v1이랑 v2랑 들러야 한다!

# 1 -> v1 -> v2 -> n weight
# 1 -> v2 -> v1 -> n weight 중 minimum을 구해라...

visited = [0] * (n+1)
dp = [2147483647] * (n+1)
dp[1] = 0
first_try = djikstra(1)

first_to_v1_dist = first_try[v1]
first_to_v2_dist = first_try[v2]

visited = [0] * (n+1)
dp = [2147483647] * (n+1)
dp[v1] = 0
v1_try = djikstra(v1)
v1_to_n_dist = v1_try[n]
v1_to_v2_dist = v1_try[v2]

visited = [0] * (n+1)
dp = [2147483647] * (n+1)
dp[v2] = 0
v2_try = djikstra(v2)
v2_to_n_dist = v2_try[n]
v2_to_v1_dist = v2_try[v1]

answer = min(first_to_v1_dist + v1_to_v2_dist + v2_to_n_dist, first_to_v2_dist + v2_to_v1_dist + v1_to_n_dist)

if answer >= 2147483647:
    print(-1)
else:
    print(answer)