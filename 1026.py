n = int(input())

a = input().split()
inta = []
for i in a:
    inta.append(int(i))
inta.sort()

b = input().split()
intb = []
for i in b:
    intb.append(int(i))
intb.sort(reverse=True)

sum = 0
for i in range(n):
    sum += inta[i] * intb[i]

print(sum)

