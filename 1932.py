ne = int(input())

dp = [[0]]

for n in range(ne):
    line = list(map(int, input().split()))

    new_line = []

    for l in range(len(line)):
        if l == 0:
            new_line.append(line[l] + dp[n][l])
        
        elif l != len(line)-1:
            new_line.append(max(line[l] + dp[n][l], line[l] + dp[n][l-1]))
        
        else:
            new_line.append(line[l] + dp[n][l-1])
    dp.append(new_line)

print(max(dp[ne]))