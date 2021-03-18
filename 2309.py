a = []
for i in range(9):
    a.append(int(input()))
    a.sort()

for i in range(9):
    for j in range(i+1, 9):
        if sum(a) - a[i] - a[j] == 100:
            del a[j]
            del a[i]

            for i in a:
                print(i)
            exit()

