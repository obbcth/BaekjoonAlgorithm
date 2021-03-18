n = int(input())

lis = []
for i in input().split():
    lis.append(int(i))

swap = 0

def merge_sort(start, end):
    global swap, lis

    size = end - start
    mid = (start + end) // 2

    if size <= 1:
        return
 
    merge_sort(start, mid)
    merge_sort(mid, end)
 
    new_lis = []
    idx1 = start
    idx2 = mid
    cnt = 0
    
    while idx1 < mid and idx2 < end:
        if lis[idx1] > lis[idx2]:
            new_lis.append(lis[idx2])
            idx2 += 1
            cnt += 1
        else: 
            new_lis.append(lis[idx1])
            idx1 += 1
            swap += cnt
    
    while idx1 < mid:
        new_lis.append(lis[idx1])
        idx1 += 1
        swap += cnt

    while idx2 < mid:
        new_lis.append(lis[idx2])
        idx2 += 1
    
    for t in range(len(new_lis)):
        lis[start + t] = new_lis[t]
 
merge_sort(0, n)
print(swap)
