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

    n = int(input())
    order = list(map(int, input().split()))
    
    graph = [[] for z in range(n+1)]
    indegree = [0 for z in range(n+1)]

    for start in range(n):
        for end in range(start+1, n):
            graph[order[start]].append(order[end])
            indegree[order[start]] += 1
    
    c = int(input())

    for __ in range(c):
        a, b = map(int, input().split())
        
        if b in graph[a]:
            graph[a].remove(b)
            graph[b].append(a)
            indegree[a] -= 1
            indegree[b] += 1
        
        elif a in graph[b]:
            graph[b].remove(a)
            graph[a].append(b)
            indegree[a] += 1
            indegree[b] -= 1
    
    err = False
    res = []
    for i in range(len(indegree)-1):
        indices = [y for y, x in enumerate(indegree[1:]) if x == i]

        if len(indices) != 1:
            err = True
            break
        else:
            res.append(indices[0]+1)

    if err:
        print("IMPOSSIBLE")
    else:
        for i in range(len(res)):
            print(f"{res[len(res)-i-1]} ", end="")
        print("")
