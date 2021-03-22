n = int(input())

d = list(map(int, input().split())) 
dic = dict()

n2 = int(input())
d2 = list(map(int, input().split())) 

for i in d:
    if dic.get(i, 0) == 0:
        dic[i] = 1
    else:
        dic[i] += 1

for i in d2:
    print(dic.get(i, 0), end=" ")
