_ = input()
s = list(map(int, input().split()))
m = max(s)
n = [i/m*100 for i in s]
print(sum(n)/len(n))