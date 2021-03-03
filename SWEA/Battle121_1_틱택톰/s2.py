import sys
sys.stdin = open('input.txt')

def IsTikTeakTom(TikTak):
    # 가로세로
    for i in range(4):
        if '.' not in TikTak[i] and 'O' not in TikTak[i]:
            return 'X won'
        if '.' not in TikTak[i] and 'X' not in TikTak[i]:
            return 'O won'

        sero = [TikTak[j][i] for j in range(4)]
        if '.' not in sero and 'O' not in sero:
            return 'X won'
        if '.' not in sero and 'X' not in sero:
            return 'O won'

    # 대각선
    rd = [TikTak[i][i] for i in range(4)]
    ld = [TikTak[i][3-i] for i in range(4)]
    if '.' not in rd and 'O' not in rd:
        return 'X won'
    elif '.' not in rd and 'X' not in rd:
        return 'O won'
    elif '.' not in ld and 'O' not in ld:
        return 'X won'
    if '.' not in ld and 'X' not in ld:
        return 'O won'

    # 미종료, 동점
    for i in range(4):
        for j in range(4):
            if TikTak[i][j] == '.':
                return 'Game has not completed'

    return 'Draw'

T = int(input())
for tc in range(1, T+1):
    TikTak = [input() for _ in range(4)]
    if tc != T: # 입력중간에 공백이 있어서 쓸데 없지만 받아둠
        blank = input()

    # 오목 판정과 유사, 4*4칸에서 가로 세로 확인은 첫행 첫열만 보면 됨
    print('#{} {}'.format(tc, IsTikTeakTom(TikTak)))
