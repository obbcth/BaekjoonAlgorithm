import math

m, n = map(int, input().split(" "))

# m 이상 n 이하의 소수 를 모두 출력해라..
for target in range(m, n+1):

    # target이 이제 소수인가 아닌가 소수이면 출력하면 된다
    flag = True

    # 1 제외
    if target == 1:
        flag = False

    for i in range(2, int(math.sqrt(target)) + 1):
        if target % i == 0:
            flag = False
            break

    if flag: print(target)
