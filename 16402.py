n, m = map(int, input().split())

# v에 대한 parent array
parent = list(range(n))

namedic = {}
nameidxtodic = {}

def find(x):
    if x == parent[x]:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    
    # 속국이 자신의 종주국 공격 -> 종주국과 속국의 parent가 이긴 속국으로 변환
    if find(x) == y:
        for _ in range(len(parent)):
            if parent[_] == y:
                parent[_] = x

    x = find(x)
    y = find(y)

    parent[y] = x


for idx in range(n):
    name = input()[11:]
    namedic[name] = idx
    nameidxtodic[idx] = name

for _ in range(m):
    a, b, w = input().split(",")
    a = a[11:]
    b = b[11:]

    a_idx = namedic[a]
    b_idx = namedic[b]

    if w == "1":
        # a wins
        union(a_idx, b_idx)
    
    if w == "2":
        # b wins
        union(b_idx, a_idx)


answer = 0
answer_arr = []

for idx in range(n):
    if idx == find(idx):
        answer += 1
        answer_arr.append(idx)

print(answer)

answer_to_ascii = [nameidxtodic[i] for i in answer_arr]
answer_to_ascii.sort()

for i in answer_to_ascii:
    print(f"Kingdom of {i}")
