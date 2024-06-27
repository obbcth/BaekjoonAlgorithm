from collections import deque

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    arr = input()

    arr = arr.replace("[", "").replace("]", "")

    if arr != "":
        arr = list(map(int, arr.split(",")))
    else:
        arr = []

    arr = deque(arr)
    flag = True

    front = True

    for func in p:
        if func == "R":
            
            if front:
                front = False
            else:
                front = True

        if func == "D":
            if len(arr) == 0:
                print("error")
                flag = False
                break
            
            if front:
                arr.popleft()
            else:
                arr.pop()
    
    if flag:
        if not front:
            arr.reverse()
        print("[" + ",".join(map(str, arr)) + "]")