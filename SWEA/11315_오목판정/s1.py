import sys
sys.stdin = open('input.txt')

def IsOmok(omok_list):
    # 행열 순회하며, 현재위치부터 가로세로대각선으로 쭉 갔을때 연속된 o가 있으면 오목!
    # 근데 오목은 5개가 연속되어야 해서 N-4 행 / N-4열까지만 보면 됨
    # 그 이후에 나오는거는 5번 이상 연속할 수가 없음

    # 가로 세로 검사
    for i in range(N-4):
        for j in range(N):
            # 세로로 검사
            if omok_list[i][j] == 'o':
                # 다음행부터,4개
                for k in range(1, 5):
                    if omok_list[i+k][j] != 'o':
                        break
                else:
                    return 'YES'

            # 가로로 검사
            if omok_list[j][i] == 'o':
                # 다음행부터,4개
                for k in range(1, 5):
                    if omok_list[j][i+k] != 'o':
                        break
                else:
                    return 'YES'

    # 오른쪽 아래 대각선
    for i in range(N-4):
        for j in range(N-4):
            if omok_list[i][j] == 'o':
                for k in range(1,5):
                    if omok_list[i+k][j+k] != 'o':
                        break
                else:
                    return 'YES'

    # 왼쪽 아래 대각선
    for i in range(N-4):
        for j in range(N-1, 3, -1):
            if omok_list[i][j] == 'o':
                for k in range(1,5):
                    if omok_list[i+k][j-k] != 'o':
                        break
                else:
                    return 'YES'

    return 'NO'


for tc in range(1, int(input())+1):
    N = int(input())
    omok_list = [list(input()) for _ in range(N)]
    print('#{} {}'.format(tc, IsOmok(omok_list)))