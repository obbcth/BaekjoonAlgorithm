n = input()

lis = n.split('-')
real_lis = []

for i in lis:
    if '+' in i:
        i2 = i.split('+')
        sum = 0
        for j in i2:
            sum += int(j)
        real_lis.append(sum)
    else:
        real_lis.append(int(i))

answer = real_lis[0]

for i in range(1, len(real_lis)):
    answer -= real_lis[i]

print(answer)

