def dfs (x, y):

    # 좌표에 도달하면 1 리턴
    if x == m-1 and y == n-1:
        return 1

    # 이미 방문한 적이 있으면 해당 값 리턴
    if dp[x][y] != -1:
        return dp[x][y]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 4방면으로 dfs 돌리기
    way = 0
    for i in range(4):
        if x + dx[i] >= 0 and y + dy[i] >= 0 and x + dx[i] < m and y + dy[i] < n and board[x][y] > board[x + dx[i]][y + dy[i]]:
            way += dfs(x + dx[i], y + dy[i])
    dp[x][y] = way
    
    return dp[x][y]


m, n = map(int, input().split()) # M N 가로 세로

board = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

print(dfs(0, 0))