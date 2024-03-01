from collections import deque

# BFS 메서드 정의
def bfs (graph, node, visited, butterfly):

    # 큐 구현을 위한 deque 라이브러리 활용
    queue = deque([node])

    # 현재 노드를 방문 처리
    visited[node] = True
    
    # 큐가 완전히 빌 때까지 반복
    while queue:

        # 큐에 삽입된 순서대로 노드 하나 꺼내기
        v = queue.popleft()

        # 탐색 순서 출력
        # print(v)
        # print(graph[v][0], graph[v][1]) # x, y

        # 만약 인접 node가 그래프에 있어:

        todo = [
            [graph[v][0] + 1, graph[v][1]],
            [graph[v][0] - 1, graph[v][1]],
            [graph[v][0], graph[v][1] + 1],
            [graph[v][0], graph[v][1] - 1]
        ]

        for t in todo:
            # print("todo: ", t)
            if t in graph:
                if not visited[graph.index(t)]:
                    queue.append(graph.index(t))
                    visited[graph.index(t)] = True
    
    # print(visited)
    # print(visited.index(False))

    if False in visited:
        bfs(graph, visited.index(False), visited, butterfly + 1)
    
    else:
        print(butterfly+1)


t = int(input())

for _ in range(t):

    m, n, k = map(int, input().split())
    # m n => 가로 세로
    # k => 배추 위치

    cabs = []
    # 배추 목록

    for _ in range(k):
        x, y = map(int, input().split())
        # x, y => 배추 좌표
        cabs.append([x, y])

    v = [False] * len(cabs)

    bfs(cabs, 0, v, 0)
