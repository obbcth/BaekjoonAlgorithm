from collections import deque

m, n, h = map(int, input().split())

all_cooked = True # 0 들어오면 False 전환

box = []
for _ in range(h):
    arr = []
    for __ in range(n):
        tomato = list(map(int, input().split()))
        arr.append(tomato)
        
        if 0 in tomato:
            all_cooked = False
    box.append(arr)

# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 없는 자리
# print(box[1][1][2]) # 높이 세로 가로

def bfs():
    global m, n, h, box
    arr = deque([])
    newarr = deque([])

    cycle = 0
    checks = [
        [1, 0, 0],
        [-1, 0, 0],
        [0, 1, 0],
        [0, -1, 0],
        [0, 0, 1],
        [0, 0, -1],
    ]

    for height in range(h):
        for y in range(n):
            for x in range(m):
                if box[height][y][x] == 1:
                    arr.append([height, y, x])
    
    while arr:
        e = arr.pop()

        for check in checks:
            if 0 <= (e[0] + check[0]) < h:
                if 0 <= (e[1] + check[1]) < n:
                    if 0 <= (e[2] + check[2]) < m:
                        if box[e[0] + check[0]][e[1] + check[1]][e[2] + check[2]] == 0:
                            box[e[0] + check[0]][e[1] + check[1]][e[2] + check[2]] = 1
                            newarr.append([e[0] + check[0], e[1] + check[1], e[2] + check[2]])

        if len(arr) == 0 and len(newarr) != 0:
            arr = newarr
            newarr = deque([])
            cycle += 1


    for height in range(h):
        for y in range(n):
            for x in range(m):
                if box[height][y][x] == 0:
                    return -1

    return cycle


if all_cooked:
    print(0)

else:
    print(bfs())

