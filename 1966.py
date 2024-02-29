from collections import deque

c = int(input())

for _ in range(c):

    n, m = map(int, input().split())
    # n = 문서의 개수
    # m = 현재 문서의 위치 (= idx 느낌으로 쓰자)

    q = deque(map(int, input().split()))
    # 문서 리스트 큐

    output = 0

    # 큐가 다 빠질때 까지
    while q:
        # 짱 큰 숫자
        big = max(q)

        # 맨 앞을 뺀다
        front = q.popleft()
        # 내가 앞으로 왔다
        m -= 1

        # 만약 맨 앞에 뺀게 짱 큰 숫자야:
        if big == front:
            # 출력이 추가가 되었다
            output += 1

            # m 값이 음수라 함은 짱 큰게 나고 내가 -1이 되었다는 말
            if m < 0:
                print(output)
                break

        # 맨 앞에 뺀게 짱 큰 숫자가 아니야:
        else:

            # 다시 집어넣는다
            q.append(front)

            # m 값이 음수라 함은 내가 빠져나왔고 그러면 다시 집어넣어야 한다
            if m < 0:
                m = len(q) - 1