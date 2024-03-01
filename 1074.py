n, y, x = map(int, input().split())

def calc(x, y, n):

    # 만약 n == 0 return
    if n == 0:
        return 0

    # 0(2^2 * 0) 4(2^2 * 1) 8(2^2 * 2) 12(2^2 * 3)
    multiplier = 0

    # x좌표가 절반보다 작아
    if x < 2 ** (n-1):

        # y좌표가 절반보다 커
        if y >= 2 ** (n-1):
            multiplier = 2
            y -= 2 ** (n-1)


    # x좌표가 절반보다 커
    else:
        x -= 2 ** (n-1)

        # y좌표가 절반보다 작아
        if y < 2 ** (n-1):
            multiplier = 1

        # y좌표가 절반보다 커
        else:
            multiplier = 3
            y -= 2 ** (n-1)
    
    return calc(x, y, n-1) + (multiplier * ((2 ** (n-1)) ** 2))


print(calc(x, y, n))

