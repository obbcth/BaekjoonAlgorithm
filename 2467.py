start = 0
end = int(input()) -1
arr = list(map(int, input().split()))

answer = 9876543210
savepos = []

while start < end:
    val = arr[start] + arr[end]

    if answer > abs(val):
        answer = abs(val)
        savepos = [start, end]
    
    if val > 0:
        end -= 1
    elif val < 0:
        start += 1
    elif val == 0:
        break

print(arr[savepos[0]], arr[savepos[1]])

