import bisect
import sys

input = sys.stdin.readline

t = int(input())

n = int(input())
n_arr = list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

x_arr = []
y_arr = []

for i in range(n):
    s = n_arr[i]
    x_arr.append(s)

    for j in range(i+1, n):
        s += n_arr[j]
        x_arr.append(s) 

for i in range(m):
    s = m_arr[i]
    y_arr.append(s)

    for j in range(i+1, m):
        s += m_arr[j]
        y_arr.append(s) 

cnt = 0

x_arr.sort()
y_arr.sort()

cnt = 0

for x in range(len(x_arr)):
    l_pos = bisect.bisect_left(y_arr, t-x_arr[x])
    r_pos = bisect.bisect_right(y_arr, t-x_arr[x])
    cnt += r_pos - l_pos        

print(cnt)