n = int(input())

for _ in range(n):
    d = int(input())
    
    arr = [[1, 0], [0, 1]]

    if d == 0 or d == 1:
        print(arr[d][0], arr[d][1])
        continue

    for i in range(d):
        if i != 0 and i != 1:            
            result = [ arr[0][0] + arr[1][0] , arr[0][1] + arr[1][1] ]

            arr[0] = arr[1]
            arr[1] = result

    print(arr[0][0] + arr[1][0] , arr[0][1] + arr[1][1])
