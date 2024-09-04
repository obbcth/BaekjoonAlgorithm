n = int(input())

arr = []
arrdic = {}
maxtime = 1

for _ in range(n):
    m = int(input())
    arr.append(m)

    if m in arrdic:
        arrdic[m] += 1
        maxtime = max(maxtime, arrdic[m])
    else:
        arrdic[m] = 1

arr = sorted(arr)

maxlist = []
for idx in arr:
    if arrdic[idx] == maxtime and idx not in maxlist:
        maxlist.append(idx)

print(round(sum(arr) / n))
print(arr[n // 2])

if len(maxlist) == 1:
    print(maxlist[0])
else:
    print(maxlist[1])

print(arr[n-1] - arr[0])