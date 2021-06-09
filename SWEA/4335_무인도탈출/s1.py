import sys
sys.stdin = open('input.txt')
import time
start = time.time()



def SOS(height, cnt, used, before_garo, before_sero):
    global max_height

    for i in range(N):
        if used[i]: continue # 이미 사용한 상자는 스킵
        a, b, c = boxes[i] # 상자의 변의 길이
        for garo, sero, h in [(b, c, a), (a, c, b), (a, b, c)]: # 높이가 a,b,c 일때 가로세로
            # 아래 상자 면적보다 작을 때 or 처음 쌓을 때
            if (garo <= before_garo and sero <= before_sero) or (garo <= before_sero and sero <= before_garo) or height == 0:
                used[i] = 1 # 사용 체크
                SOS(height + h, cnt + 1, used, garo, sero)
                used[i] = 0 # 체크 해제


    if  height > max_height:
        max_height = height


for tc in range(1, int(input())+1):
    N = int(input())
    boxes = [list(map(int, input().split())) for _ in range(N)]

    # 상자의 순서, 상자의 높이 -> n개 상자에 대해서 최대 n!*3^n 번 연산필요 (완전탐색)

    max_height = 0

    used = [0] * N
    SOS(0, 0, used, 0, 0)

    print('#{} {}'.format(tc, max_height))
    # print(f'#{tc} {max_height}')



print((time.time() - start))