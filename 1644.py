n = int(input())

primeList = []
eratos = [0] * (n+1)

for i in range(2, n+1):
    if eratos[i] == 0:
        primeList.append(i)
    
    for j in range(i, n+1, i):
        eratos[j] = 1
        
count = 0

sum = 0
start = 0
end = 0

while True:
    if sum >= n:
        if sum == n:
            count += 1
        sum -= primeList[start]
        start += 1
    elif end == len(primeList):
        break
    else:
        sum += primeList[end]
        end += 1

print(count)
