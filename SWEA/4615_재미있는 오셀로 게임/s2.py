import sys
from pandas import DataFrame as df
sys.stdin = open("eval_input.txt")

def Othello(N, M, location):
    # 놓아진 돌에서 8방향 확인했을때, 다른 색돌이 쭉 있다가,
    # 같은 색돌로 막아져있어야 그 사이에 있는 다른색돌을 내꺼로 만들 수 있음
    # 예) 00012221000 이렇게 있어야 사이의 2를 1로 교환가능
    # 예) 00012222000 이러면 1과 1사이에 2가 있는게 아니라서 교환불가
    # 주의! 연속된게 여러개이더라도, 그 끝에 내돌과 같은 색돌 있으면 그 사이의 모든 돌 교환가능

    # 보드 초기화
    # 상하좌우에 1칸씩 쿠션을 만들어서 인덱스 오류를 사전에 차단하자!
    board = [[0]*(N+2) for _ in range(N+2)]

    # 초기 흑백 돌 놓기
    board[N // 2][N // 2] = 2 # 백
    board[N // 2 + 1][N // 2 + 1] = 2 # 백
    board[N // 2 + 1][N // 2] = 1 # 흑
    board[N // 2][N // 2 + 1] = 1 # 흑
    #print(df(board))

    # 상 하 좌 우 4방향 대각선, 연속된 돌 확인용
    dx = [1, -1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]

    # 턴수만큼 게임진행하기
    for i in range(M):
        # 주어진 input대로 해당 위치에 돌 놓기
        x = location[i][0]
        y = location[i][1]
        stone = location[i][2]
        board[x][y] = stone

        # 내 돌이랑 반대돌을 other라고 하자
        if stone == 1:
            other = 2
        else:
            other = 1

        # 8개의 방향으로 확인하자
        for j in range(8):
            # 현재 방향으로 한칸씩 더가면서, 어떤 색의 돌이 있는지 확인하기 위함
            k = 1
            while k < N:
                # 새로 놓아진 돌 위치에서 한칸 갔을 때 돌이 다른 색이면, 그 다음을 또 확인해야함
                if board[x + k*dx[j]][y + k*dy[j]] == other:
                    k += 1
                # 한칸 가서 확인했는데, 그 위치에 돌이 없거나(0), 같은 색이면 중지(stone)
                else:
                    break

            # 11,22 이런식으로 바로 같은 돌이 나온게 아니고 (k > 1)
            # 마지막으로 다른색돌이 아니여서 탈출했던 K 거리를 간곳의 돌 색깔이 나랑 같으면
            # 그 사이의 돌들의 색을 다 내꺼로 바꿔줘야함
            # 예) 12221 이면 K=4 이고 k가 1~3을 1로 바꿔줘야함
            # 예
            if k > 1 and board[x + k*dx[j]][y + k*dy[j]] == stone:
                for kk in range(1, k):
                    board[x + kk * dx[j]][y + kk * dy[j]] = stone


    #print(df(board))
    # 모든 턴이 진행된 이후에 흑백돌 세기
    black_1_cnt = 0
    white_2_cnt = 0
    for i in range(1, N + 1): # 앞뒤 쿠션 빼고 세기
        for j in range(1, N + 1):
            if board[i][j] == 1:
                black_1_cnt += 1
            elif board[i][j] == 2:
                white_2_cnt += 1

    return black_1_cnt, white_2_cnt


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    location = [ list(map(int, input().split())) for i in range(M) ]
    print('#{} {}'.format(tc, ' '.join(map(str, Othello(N, M, location)))))

