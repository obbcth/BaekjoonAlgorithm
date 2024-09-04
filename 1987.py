import sys
input = sys.stdin.readline

r, c = map(int, input().split())

m = []
for _ in range(r):
    m.append(input())


visited_alphabet = [0] * 26
max_len = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, count):
    global max_len
    max_len = max(max_len, count)

    for _ in range(4):
        if (0 <= x + dx[_] < r) and (0 <= y + dy[_] < c):
            if visited_alphabet[ord(m[x + dx[_]][y + dy[_]])-65] == 0:
                visited_alphabet[ord(m[x + dx[_]][y + dy[_]])-65] = 1
                dfs(x + dx[_], y + dy[_], count+1)
                visited_alphabet[ord(m[x + dx[_]][y + dy[_]])-65] = 0


visited_alphabet[ord(m[0][0])-65] = 1
dfs(0, 0, 1)

print(max_len)