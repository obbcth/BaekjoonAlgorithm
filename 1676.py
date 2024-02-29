n = int(input())

count_2 = 0
count_5 = 0

def divide(num, i):
    if num % i == 0:
        return divide(num // i, i) + 1
    else:
        return 0

for i in range(2, n+1):
    count_2 += divide(i, 2)
    count_5 += divide(i, 5)

print(min(count_2, count_5))
