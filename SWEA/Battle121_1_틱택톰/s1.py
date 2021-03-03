import sys
sys.stdin = open('input.txt')

def IsTikTeakTom(TikTak):
    # 오목 검사와 유사

    # 1. 가로세로 검사 (첫행 첫열만 보면 됨)
    for i in range(1):
        for j in range(4):
            # 세로 확인
            if TikTak[i][j] != '.':
                who = TikTak[i][j]
                for k in range(1, 4):
                    if TikTak[i+k][j] != who and TikTak[i+k][j] != 'T':
                        break
                else:
                    return '{} won'.format(who)
            # 가로 확인
            if TikTak[j][i] != '.':
                who = TikTak[j][i]
                for k in range(1, 4):
                    if TikTak[j][i+k] != who and TikTak[j][i+k] != 'T':
                        break
                else:
                    return '{} won'.format(who)

    # 2. 대각선 검사 (0,0 과 0,3 만 보면 됨)
    rd = 0
    ld = 0
    if TikTak[0][0] != '.':
        who = TikTak[0][0]
        for k in range(1, 4):
            if TikTak[k][k] == who or TikTak[k][k] == 'T':
                rd += 1
        if rd == 3:
            return '{} won'.format(who)

    if TikTak[0][3] != '.':
        who = TikTak[0][3]
        for k in range(1, 4):
            if TikTak[k][3-k] == who or TikTak[k][3-k] == 'T':
                ld += 1
        if ld == 3:
            return '{} won'.format(who)

    # 3. 아직도 안끝난 경우
    # '.' 이 하나라도 있으면 미종료
    for i in range(4):
        for j in range(4):
            if TikTak[i][j] == '.':
                return 'Game has not completed'

    # 위에서 한번도 안걸리고 여기까지 왔다면 동점
    return 'Draw'

T = int(input())
for tc in range(1, T+1):
    TikTak = [input() for _ in range(4)]
    if tc != T: # 입력중간에 공백이 있어서 쓸데 없지만 받아둠
        blank = input()

    # 오목 판정과 유사, 4*4칸에서 가로 세로 확인은 첫행 첫열만 보면 됨
    print('#{} {}'.format(tc, IsTikTeakTom(TikTak)))
