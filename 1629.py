a, b, c = map(int,  input().split())

def 제곱(a, b):
    if b == 1:
        return a % c
    else:
        temp = 제곱(a, b // 2)
        if b % 2 == 0:
            return temp * temp % c
        else:
            return temp * temp * a % c

print(제곱(a, b))
