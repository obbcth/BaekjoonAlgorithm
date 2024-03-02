import sys
import heapq

n = int(sys.stdin.readline())

leftheap = []
rightheap = []

for _ in range(n):
    test = int(sys.stdin.readline())

    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, (-test, test))
    else:
        heapq.heappush(rightheap, (test, test))


    if rightheap and leftheap[0][1] > rightheap[0][0]:

        m = heapq.heappop(rightheap)[0]
        n = heapq.heappop(leftheap)[1]

        heapq.heappush(leftheap, (- m , m ))
        heapq.heappush(rightheap, ( n , n ))

    print(leftheap[0][1])