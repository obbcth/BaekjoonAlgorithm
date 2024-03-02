from bisect import bisect_left

n = int(input())
# 보고 싶은 채널 번호

m = int(input())
# 고장난 버튼 개수

broken = []

if m != 0:
    broken = input().split()

channelList = []

for channelNumInit in range(1000001):

    if channelNumInit >= 99 and channelNumInit <= 102:
        channelList.append(channelNumInit)
        continue

    able = True
    for button in broken:
        if button in str(channelNumInit):
            able = False
            break

    if able:
        channelList.append(channelNumInit)

idx = bisect_left(channelList, n)

a = idx - 1
b = idx
c = idx + 1

count = []

# 예상되는 시나리오.. 100에서 +를 했는데 그게 버튼 개수가 적은거임..!
# 99면 1번
# 100면 0번
# 101은 1번
# 102면 2번

if a != -1:
    if channelList[a] == 99:
        count.append(abs(channelList[a] - n) + 1)
    elif channelList[a] == 100:
        count.append(abs(channelList[a] - n))
    elif channelList[a] == 101:
        count.append(abs(channelList[a] - n) + 1)
    elif channelList[a] == 102:
        count.append(abs(channelList[a] - n) + 2)
    else:
        count.append(len(str(channelList[a])) + abs(channelList[a] - n))

if b < len(channelList):
    if channelList[b] == 99:
        count.append(abs(channelList[b] - n) + 1)
    elif channelList[b] == 100:
        count.append(abs(channelList[b] - n))
    elif channelList[b] == 101:
        count.append(abs(channelList[b] - n) + 1)
    elif channelList[b] == 102:
        count.append(abs(channelList[b] - n) + 2)
    else:
        count.append(len(str(channelList[b])) + abs(channelList[b] - n))

if c < len(channelList):
    if channelList[c] == 99:
        count.append(abs(channelList[c] - n) + 1)
    elif channelList[c] == 100:
        count.append(abs(channelList[c] - n))
    elif channelList[c] == 101:
        count.append(abs(channelList[c] - n) + 1)
    elif channelList[c] == 102:
        count.append(abs(channelList[c] - n) + 2)
    else:
        count.append(len(str(channelList[c])) + abs(channelList[c] - n))

print(min(count))