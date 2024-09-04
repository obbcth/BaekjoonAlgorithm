import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline

n = int(input())

edges = [[] for _ in range(n+1)]

for _ in range(n):
    vertex = input().split()

    for i in range( (len(vertex)-2) // 2):
        
        v = int(vertex[0])
        u = int(vertex[(i+1)*2-1])
        w = int(vertex[(i+1)*2])

        edges[v].append([u, w])

def dfs(start, weight):
    for edge in edges[start]:
        if visited[edge[0]] == -1:
            visited[edge[0]] = weight+edge[1]
            dfs(edge[0], weight+edge[1])

visited = [-1] * (n+1)
visited[1] = 0
dfs(1, 0)

new_start = [0, 0]
for i in range(len(visited)):
    if visited[i] > new_start[1]:
        new_start[1] = visited[i]
        new_start[0] = i

visited = [-1] * (n+1)
visited[new_start[0]] = 0
dfs(new_start[0], 0)

print(max(visited))