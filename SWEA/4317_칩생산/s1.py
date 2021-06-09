import sys
sys.stdin = open('input.txt')
import time
start = time.time()


def Chip(wafer, cnt, before_r, before_c):
    global max_cnt, dp

    if cnt > max_cnt:
        max_cnt = cnt

    if cnt:
        if before_r > dp_cnt[cnt] and cnt < dp_loca[(before_r, before_c)]:
            return

        dp_cnt[cnt] = before_r
        dp_loca[(before_r, before_c)] = cnt

    for r in range(before_r, R-1):
        for c in range(C-1):
            if wafer[r][c] or wafer[r + 1][c] or wafer[r][c + 1] or wafer[r + 1][c + 1]: continue

            for x, y in [(0, 0), (1, 0), (0, 1), (1, 1)]: # 방문체크
                wafer[r + x][c + y] = 1

            Chip(wafer, cnt + 1, r, c)

            for x, y in [(0, 0), (1, 0), (0, 1), (1, 1)]: # 방문체크 해제
                wafer[r + x][c + y] = 0


for tc in range(1, int(input()) + 1):
    R, C = map(int, input().split())

    wafer = [list(map(int, input().split())) for _ in range(R)]

    # R*C 순회하면서 현재 좌표에 칩을 만들 수 있는지 없는지 판단 -> 방해물 없고, 칩으로 만들지 않은 곳
    # 최대 갯수라서 전체 다 순회해야 하고, 따로 방문체크 만들 필요없이 직접 wafer에 쓰고 빼는 식으로 해도 될듯
    # 재귀로 구현

    max_cnt = 0
    limit = R // 2 * C // 2
    dp_cnt = [R*2] * limit
    dp_loca = dict()
    for i in range(R):
        for j in range(C):
            dp_loca[(i, j)] = -1
    Chip(wafer, 0, 0, 0)
    print('#{} {}'.format(tc, max_cnt))

print((time.time() - start))