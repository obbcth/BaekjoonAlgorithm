from collections import deque

t = int(input())

def topology_sort(v, graph, indegree):
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    return result

for _ in range(t):
    dp = {}
    n, k = map(int, input().split())

    indegree = [0] * (n + 1)

    time_to_construct_list = list(map(int, input().split()))
    order_to_construct = []

    graph = [[] for i in range(n + 1)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        order_to_construct.append([a, b])
        indegree[b] += 1

    w = int(input())
    out = topology_sort(n, graph, indegree)

    for idx in out: 
        for lis in order_to_construct:            
            if lis[0] == idx:

                if lis[0] not in dp:
                    dp[lis[0]] = time_to_construct_list[idx-1]

                if lis[1] in dp:
                    dp[lis[1]] = max(dp[lis[1]], dp[lis[0]] + time_to_construct_list[lis[1] - 1])
                else:
                    dp[lis[1]] = dp[lis[0]] + time_to_construct_list[lis[1] - 1]
                
    if w in dp:
        print(dp[w])
    else:
        print(time_to_construct_list[w-1])
