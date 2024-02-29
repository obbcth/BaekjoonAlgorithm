n = int(input())

result_arr = [i for i in range(1, n+1)] # 얘는 queue 마냥 쓰고
temp_arr = [] # 얘는 stack 마냥 쓸거임

print_queue = []

# 구현이 불가능한 수열이야
flag = True

# n의 개수만큼 지금 수열이 만들어져 있어요
for _ in range(n):
    target = int(input())
    # temp_arr에 target이 없다
    # result_arr에서 계속 끌어다 와
    if target not in temp_arr:
        while target not in temp_arr:
            temp_arr.append(result_arr.pop(0))
            print_queue.append("+")
    
        # 다 끌어왔어 그러면
        # result_arr 맨 뒤에 배치
        result_arr.append(temp_arr.pop())
        print_queue.append("-")
    
    # temp_arr에 target이 있어
    else:

        # 만약 temp_arr의 마지막 부분의 것이 target이 아니야
        if target != temp_arr[-1]:
            # 구현이 안되는 수열이다!
            print("NO")
            flag = False
            break
        
        else:
            # result_arr 맨 뒤에 배치
            result_arr.append(temp_arr.pop())
            print_queue.append("-")


# 구현이 가능한거야? -> 무조건 구현이 가능하다
if flag:
    for p in print_queue:
        print(p)
