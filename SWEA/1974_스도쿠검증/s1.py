import sys
sys.stdin = open("input.txt")

def issdoku(sdoku):
    # 가로, 세로 1~9가 각 한번씩만 나와야한다
    is_sdoku = [1] * 9 # 1~9의 카운트를 센 것 / 스도쿠 판별을 위한 리스트
    for i in range(9):
        r_counter = [0] * 9
        c_counter = [0] * 9
        for j in range(9):
            r_counter[sdoku[i][j]-1] += 1
            c_counter[sdoku[j][i]-1] += 1
        if r_counter != is_sdoku or c_counter != is_sdoku:
            return 0

    # 3*3 칸에서도 1~9가 한번씩만 나와야한다.
    # i의 범위 0~3 / 3~6 / 6~9
    # j의 범위 0~3 / 3~6 / 6~9
    # 0~3의 범위의 배수를 지정해줄 행렬 보조 인덱스 k,l을 추가
    for k in range(3):
        for l in range(3):
            counter = [0] * 9
            for i in range(3*k, 3*(k+1)):
                    for j in range(3*l, 3*(l+1)):
                        counter[sdoku[i][j]-1] += 1
            if counter != is_sdoku:
                return 0

    return 1


for tc in range(1, int(input())+1):
    sdoku = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(tc, issdoku(sdoku)))