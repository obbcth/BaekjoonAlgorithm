from bisect import bisect_left

n, d = map(int, input().split()) 

석순 = []
종유석 = []

for i in range(n):
    if i % 2 == 0:
        석순.append(int(input()))
    else:
        종유석.append(int(input()))

석순.sort()
종유석.sort()

a = len(석순)
b = len(종유석)

answer = a + b
answer_n = 1

for i in range(1, d+1):
    brk = a + b - bisect_left(석순, i) - bisect_left(종유석, d - i + 1)

    if answer > brk:
        answer = brk
        answer_n = 1
    elif answer == brk:
        answer_n += 1

print(answer, answer_n)
