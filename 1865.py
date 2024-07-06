tc = int(input())


def bf():
    for i in range(n):
        for j in range(len(edges)):
            cur, next, cost = edges[j]

            if dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost

                if i == n-1:
                    return True

    return False


for __ in range(tc):

    n, m, w = map(int, input().split())

    dist = [999999999] * (n+1)
    edges = []


    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, (-1)*t))

    if bf():
        print("YES")
    else:
        print("NO")
