import math

n = int(input())

coordinate = [[], ]

# n개의 별이 주어졌을 때 가능한 간선의 경우
# 2개 -> 1 3개 -> 3 4개 -> 6 .. -> n n-1 / 2

# v에 대한 parent array
parent = list(range(n+1))

vertex = []

def pt(a, b):
    a_x, a_y = coordinate[a]
    b_x, b_y = coordinate[b]

    dis_2 = (b_x-a_x)**2 + (b_y-a_y)**2
    return math.sqrt(dis_2)

def find(x):
    if x == parent[x]:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if y < x:
        parent[x] = y
    else:
        parent[y] = x


for _ in range(n):
    x, y = map(float, input().split())
    coordinate.append([x, y])

if n == 1:
    print("0.0")

else:
    

    for i in range(1, n+1):
        for j in range(1, i+1):
            # i, j 사이 간격

            if i != j:
                value = pt(i, j)
                vertex.append([i, j, value])

    vertex = sorted(vertex, key=lambda x:x[2])


    sum = 0

    for item in vertex:
        value = item[2]
        x = item[0]
        y = item[1]

        if find(x) == find(y):
            pass
        else:
            sum += value
            union(x, y)

    print(sum)

