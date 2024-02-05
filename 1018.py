n, m = map(int, input().split())

board = []

for i in range(n):
    board.append(input())

answer = 999999999

for y in range(n - 7):
    for x in range(m - 7):
        
        cnt_odd = 0
        cnt_even = 0

        for i in range(8):
            for j in range(8):
                
                if (y+i + x+j) % 2 == 0: # 홀수 좌표

                    if board[y+i][x+j] == "W": # 홀수 칸에 W가 있다
                        cnt_odd += 1 # B로 만들어버리겠다 -> 짝수 칸은 W가 된다

                    if board[y+i][x+j] == "B": # 홀수 칸에 B가 있다
                        cnt_even += 1 # W로 만들어버리겠다

                else: # 짝수 좌표

                    if board[y+i][x+j] == "W": # 짝수 칸에 W가 있다
                        cnt_even += 1 # B로 만들어버리겠다 -> 홀수 칸은 W가 된다

                    if board[y+i][x+j] == "B":
                        cnt_odd += 1
        
        answer = min(cnt_odd, cnt_even, answer)

print(answer)

                
