import heapq

n = int(input())

heap = []

for _ in range(n):
    heapq.heappush(heap, -int(input()))

a = -heapq.heappop(heap)
b = -heapq.heappop(heap)
c = -heapq.heappop(heap)

while True:
    if (a < b + c):
        print(a + b + c)
        break

    if len(heap) == 0:
        print(-1)
        break

    a = b
    b = c
    c = -heapq.heappop(heap)
