import sys
sys.stdin = open("eval_input.txt")

def Rogguggeo(n, board):
    roggu_cnt = 0 # 가로 세로 총 회문 카운트
    for i in range(8): # 판 사이즈 8*8 고정
        for j in range(8-n+1): # 구간합
            # 가로세로 동시판별을 위해 각각 선언
            r_temp = 0
            c_temp = 0
            for k in range(n//2):
                # 앞뒤 일치가 있을 경우 카운트
                if board[i][j+k] == board[i][j+n-1-k]:
                    r_temp += 1
                if board[j+k][i] == board[j+n-1-k][i]:
                    c_temp += 1
            # 반복문 내에서 모두 일치가 되어서, 카운트가 전체 다 세어진 경우 = 회문
            if r_temp == n//2:
                roggu_cnt += 1
            if c_temp == n//2:
                roggu_cnt += 1

    return roggu_cnt

for tc in range(1, 11):
    n = int(input())
    board = [ input() for _ in range(8)]
    print('#{} {}'.format(tc, Rogguggeo(n, board)))