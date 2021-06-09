import sys
sys.stdin = open('input.txt')
import time
start = time.time()


def SOS(height, cnt, used, before_garo, before_sero):
    global max_height

    #1-1. ☆ 백트래킹 : 유망성 검사 ☆
    # 동일한 갯수를 쌓았을때, 높이도 낮고 면적도 작으면 유망하지 않다.
    if height <= status[cnt][0]:
        if (before_garo <= status[cnt][1] and before_sero <= status[cnt][2]) or (before_sero <= status[cnt][1] and before_garo <= status[cnt][2]):
            return

    #1-2. 유망하면 status 갱신
    status[cnt] = [height, before_garo, before_sero]

    #2. 완전탐색
    for i in range(N):
        if used[i]: continue # 이미 사용한 상자는 스킵
        a, b, c = boxes[i] # 세 변의 길이
        for garo, sero, h in [(b, c, a), (a, c, b), (a, b, c)]:
            # 아래 상자 면적보다 작을 때 or 처음 쌓을 때
            if height == 0 or (garo <= before_garo and sero <= before_sero) or (garo <= before_sero and sero <= before_garo):
                used[i] = 1 # 사용 체크
                SOS(height + h, cnt + 1, used, garo, sero)
                used[i] = 0 # 체크 해제

    #3. 결과
    if  height > max_height:
        max_height = height


for tc in range(1, int(input())+1):
    N = int(input())
    boxes = [list(map(int, input().split())) for _ in range(N)]

    # 상자의 순서, 상자의 높이
    # n개 상자에 대해서 최대 n!*3^n 번 연산필요 (완전탐색)
    # 그냥 하면 시간초과 -> 백트래킹 필요

    max_height = 0
    used = [0] * N
    status = [[0, 0, 0]] * (N+1)

    SOS(0, 0, used, 1, 1)

    print('#{} {}'.format(tc, max_height))
    # print(f'#{tc} {max_height}')



print((time.time() - start))