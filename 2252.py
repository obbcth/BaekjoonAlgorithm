from collections import deque

n, k = map(int, input().split())

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


dp = {}

indegree = [0] * (n + 1)
graph = [[] for i in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

out = topology_sort(n, graph, indegree)
print(" ".join(map(str, out)))