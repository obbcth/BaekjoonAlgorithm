n, r, q = map(int, input().split())

# 트리의 간선을 인접 리스트로 표현
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [0] * (n+1)

def dfs(p):
    visited[p] = 1
    print(p)
    
    for neighbor in adj[p]:
        if not visited[neighbor]:
            dfs(neighbor)

# 쿼리 처리
visited[r] = 1  # 루트 노드는 이미 방문 처리
dfs(r)

for _ in range(q):
    u = int(input())