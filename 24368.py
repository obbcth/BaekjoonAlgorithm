a2, a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())

# case 1
# a2 - c > 0
if (a2 > c):
    print(0)


# case 2
# a2 - c == 0
elif (a2 == c):

    # a1 > 0
    if (a1 > 0):
        print(0)
    
    # a1 == 0
    elif (a1 == 0):
        # a0 <= 0 -> legit
        if (a0 <= 0):
            print(1)
        else:
            print(0)
    
    # a1 < 0
    else:
        # 위로 향하는 그래프의 경우
        # n0를 n에 대입해서 0보다 작거나 같은지 확인
        if (a1 * n0 + a0 <= 0):
            print(1)
        else:
            print(0)

# case 3
# a2 - c < 0
else:
    # 변곡점의 x좌표는 a1 / 2(a2-c)
    # 이게 일단 n0과 비교를 해봐야됨

    x = a1 / (2 * (c-a2))
    y = (a1 * a1 - 4 * a0 * (a2-c)) / (4 * (a2-c)* (a2-c))

    if (y <= 0):
        print(1)
    
    else:

        if (x < n0):
            if ((a2-c)*n0*n0 + a1*n0 + a0 <= 0):
                print(1)
            else:
                print(0)
        
        else:
            if ((a2-c)*x*x + a1*x + a0 <= 0):
                print(1)
            else:
                print(0)
