_ = input()
a = set(map(int, input().split(" "))) # list로 하면 시간초과가 난다..
_ = input()
b = list(map(int, input().split(" ")))

[print(1 if i in a else 0) for i in b]
