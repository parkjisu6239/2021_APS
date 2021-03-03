import sys
sys.stdin = open('input.txt', 'r', encoding = 'UTF-8')

def Uiseog(board):
    result = ''
    # 각 행의 문자열 길이는 최대 15개(열 인덱스는 0~14까지 가능)
    for j in range(15):
        # 행은 무조건 5개
        for i in range(5):
            # 각행의 문자열 길이는 서로 다를 수 있으므로,
            # 그 행의 길이가 j보다 클때만 결과에 더한다.
            # 즉, 그 행의 문자열길이만큼만 더하고, j가 문자열 길이를 넘어가면 실행하지 않는다
            if len(board[i]) > j:
                result += str(board[i][j])
    return result

for tc in range(1, int(input())+1):
    board = []
    for _ in range(5):
        board.append(input())
    print('#{} {}'.format(tc, Uiseog(board)))