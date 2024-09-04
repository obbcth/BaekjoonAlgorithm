n = int(input())

base = [
    "  *  ",
    " * * ",
    "*****"
]

def p():
    for _ in base:
        print(_)

def do(idx):
    if idx == 3:
        p()
    else:

        n = len(base)
        for _ in range(n):
            base.append(base[_] + " " + base[_])
            base[_] = " " * n + base[_] + " " * n

        do(idx//2)

do(n)