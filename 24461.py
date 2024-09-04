from collections import deque, defaultdict

n = int(input())
cnt = [0] * n
edges = defaultdict(set)

for i in range(1, n):
    a, b = map(int, input().split())

    cnt[a] += 1
    cnt[b] += 1
    edges[a].add(b)
    edges[b].add(a)

q = deque()
remain = set()
remainCnt = 0
exceptionChk = 0

for i in range(n):
    if cnt[i] == 1:
        q.append(i)
    elif cnt[i] == 2:
        exceptionChk += 1
    elif cnt[i] >= 3:
        remain.add(i)
        remainCnt += 1

solo = False

while remainCnt != 0:
    if remainCnt == 1 and exceptionChk == 0:  # exception case
        print(next(iter(remain)))
        solo = True
        break

    next_q = deque()

    while q:
        cur = q.popleft()
        opposite = next(iter(edges[cur]))

        cnt[cur] -= 1
        if cnt[cur] == 1:
            exceptionChk -= 1
        if cnt[cur] == 2:
            exceptionChk += 1

        cnt[opposite] -= 1

        if cnt[opposite] == 1:
            exceptionChk -= 1
            next_q.append(opposite)
        if cnt[opposite] == 2:
            exceptionChk += 1
        if cnt[opposite] < 3 and opposite in remain:
            remain.remove(opposite)
            remainCnt -= 1

        edges[opposite].remove(cur)

    q = next_q


if not solo:
    result = []
    for i in range(n):
        if cnt[i] > 0:
            result.append(str(i))
    print(" ".join(result))
