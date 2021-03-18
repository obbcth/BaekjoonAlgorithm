n = int(input())

column = []
for i in range(n):
    column.append(list(map(int, input().split())))

column.sort(key = lambda x:x[0])  # 끝나는 시간 기준으로 정렬
column.sort(key = lambda x:x[1])  # 끝나는 시간 기준으로 정렬

회의개수 = 0
startkey = 0

for i in column:
    if i[0] >= startkey:
        회의개수 += 1
        startkey = i[1]

print(회의개수)
