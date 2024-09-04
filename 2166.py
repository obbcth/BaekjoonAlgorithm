n = int(input())
shoelaces = []
for _ in range(n):
    a, b = map(int, input().split())
    shoelaces.append([a, b])

sum = 0
for i in range(n-1):
    sum += shoelaces[i][0] * shoelaces[i+1][1] - shoelaces[i][1] * shoelaces[i+1][0]
sum += shoelaces[n-1][0] * shoelaces[0][1] - shoelaces[n-1][1] * shoelaces[0][0]

print(round(abs(sum/2), 1))
