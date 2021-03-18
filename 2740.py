a세로, a가로 = list(map(int, input().split()))
a행렬 = []
for i in range(a세로):
    a행렬.append(list(map(int, input().split())))

b세로, b가로 = list(map(int, input().split()))
b행렬 = []
for i in range(b세로):
    b행렬.append(list(map(int, input().split())))

행렬 = [[0 for col in range(b가로)] for row in range(a세로)]

for i in range(a세로):
    for j in range(b가로):
        for k in range(a가로):
            행렬[i][j] += a행렬[i][k] * b행렬[k][j]

for i in 행렬:
    print(' '.join(list(map(str, i))))
