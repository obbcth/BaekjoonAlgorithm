n, m = map(int, input().split())

matrix = []
for _ in range(n):
    box = list(map(int, input().split()))

    
    if _ == 0:
        for __ in range(1, len(box)):
            box[__] += box[__-1]
    else:
        box[0] += matrix[_-1][0]
        for __ in range(1, len(box)):
            box[__] += box[__-1] + matrix[_-1][__] - matrix[_-1][__-1]

    matrix.append(box)

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    if x1 > 1 and y1 > 1:
        print(matrix[x2-1][y2-1] - matrix[x1-2][y2-1] - matrix[x2-1][y1-2] + matrix[x1-2][y1-2])
    
    elif x1 <= 1 and y1 > 1:
        print(matrix[x2-1][y2-1] - matrix[x2-1][y1-2])

    elif x1 > 1 and y1 <= 1:
        print(matrix[x2-1][y2-1] - matrix[x1-2][y2-1])
    
    elif x1 <= 1 and y1 <= 1:
        print(matrix[x2-1][y2-1])