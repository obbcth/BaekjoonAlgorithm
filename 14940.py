n, m = list(map(int, input().split()))

# n, m  2 <= 1000
# 0 > 갈수없음
# 1 > 갈수있음
# 2 > 목표지점, 단 한개
# 가로 세로로만 움직일 수 있음

# 갈 수 없는 땅 -> 0
# 갈 수 있는데 도달하지 못하다 -> -1

visit = [[-1 for _ in range(m)] for _ in range(n)]
jido = []

startpos = {
}

for _ in range(n):

    lis = list(map(int, input().split()))
    if 2 in lis:
        startpos["m"] = lis.index(2)
        startpos["n"] = _

    jido.append(lis)


def bfs(x, y):
    queue = [(x, y)]
    visit[x][y] = 0

    while queue:
        v = queue[0]
        del queue[0]

        # 현재 좌표를 딱 때리다

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            if v[0] + dx[i] < n and v[0] + dx[i] >= 0 and v[1] + dy[i] < m and v[1] + dy[i] >= 0 and visit[v[0]+dx[i]][v[1]+dy[i]] == -1:
                if jido[v[0]+dx[i]][v[1]+dy[i]] == 0:
                    visit[v[0]+dx[i]][v[1]+dy[i]] = 0
                else:
                    visit[v[0]+dx[i]][v[1]+dy[i]] = visit[v[0]][v[1]] + 1
                    queue.append( (v[0]+dx[i], v[1]+dy[i]) )

    return visit
       

result = bfs(startpos["n"], startpos["m"])

for x in range(n):
    for y in range(m):
        if jido[x][y] == 0:
            print(0, end=" ")
        else:
            print(result[x][y], end=" ")
    print()

