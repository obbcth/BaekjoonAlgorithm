import sys
sys.setrecursionlimit(10**6)

v, e = map(int, input().split())

# v에 대한 parent array
parent = list(range(v+1))

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

arr = []
for _ in range(e):
    a, b, c = map(int, input().split())
    arr.append([c, a, b])


arr = sorted(arr, key=lambda x: x[0])
sum = 0

for item in arr:
    value = item[0]
    x = item[1]
    y = item[2]

    if find(x) == find(y):
        pass
    else:
        sum += value
        union(x, y)

print(sum)
