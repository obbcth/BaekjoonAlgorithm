from collections import deque

# BFS 메서드 정의
def bfs (graph, node, visited):

    # 큐 구현을 위한 deque 라이브러리 활용
    queue = deque([node])

    # 현재 노드를 방문 처리
    visited[node] = True
    
    # 큐가 완전히 빌 때까지 반복
    while queue:
        
        # 큐에 삽입된 순서대로 노드 하나 꺼내기
        v = queue.popleft()

        # graph [v] 대신에 v를 원소로 가지는 걸로 바꿔서

        for idx in range(len(graph)):

            if graph[idx][0] - 1 == v:

                if not visited[graph[idx][1] - 1]:
                    queue.append(graph[idx][1] - 1)
                    visited[graph[idx][1] - 1] = True

    print(sum(visited) - 1)

n = int(input()) # 컴퓨터 수

connections = int(input()) # 노드 개수
connectionList = []

for _ in range(connections):

    connect = list(map(int, input().split()))

    connectionList.append(connect)
    connectionList.append(list(reversed(connect)))

visitedComputers = [False] * n

bfs(connectionList, 0, visitedComputers)