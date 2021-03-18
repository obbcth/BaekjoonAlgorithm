n, m, b = input().split()

n = int(n)
m = int(m)
b = int(b)

total = []

for i in range(n):
    total.append(list(map(int, input().split()))  )

# n 세로
# m 가로
# b 땅가진거

max_time = 9999999999999999999
end_floor = 0

for start_floor in range(257):

    pain = 0
    remain = 0

    for i in range(n):
        for j in range(m):
            
            if total[i][j] < start_floor:
                pain += start_floor - total[i][j]
            
            else:
                remain += total[i][j] - start_floor
    
    if pain > remain + b:
        continue

    time = pain + remain*2
    if time <= max_time:
        max_time = time
        end_floor = start_floor

print(max_time, end_floor)
    
