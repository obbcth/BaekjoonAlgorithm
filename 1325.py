from collections import deque
import sys

# TIMEOUT!

n, m = map(int, sys.stdin.readline().split())

edge = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    edge.append((a, b))

def bfs(v):
    queue = deque([v])

    visited = [0] * (n+1)
    visited[v] = 1
    pcnum = 0
    
    while queue:
        q = queue.popleft()
        pcnum += 1

        for i in edge:
            if i[1] == q and visited[i[0]] == 0:
                queue.append(i[0])
                visited[i[0]] == 1
    
    return pcnum

max = 0
answer = []

for start in range(1, n+1):
    result = bfs(start)

    if max < result:
        max = result
        answer = [start]
    
    elif max == result:
        answer.append(start)

print(" ".join(map(str, answer)))
