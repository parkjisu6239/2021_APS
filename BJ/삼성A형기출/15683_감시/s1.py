import sys
sys.stdin = open('input.txt')
q = lambda: map(int, sys.stdin.readline().split())

N, M = q()
cctv = [list(q()) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def getCctvArea(r, c, no):
    cctv_area_cnt = [0, 0, 0, 0]
    cctv_area = [{(r, c)} for _ in range(4)]

    for k in range(4):
        cnt = 0
        nr, nc = r, c

        while True:
            nr += dr[k]
            nc += dc[k]
            if 0 <= nr < N and 0 <= nc < M and (not cctv[nr][nc] == 6):
                if checked[nr][nc] == 0:
                    cnt += 1
                    cctv_area[k].add((nr, nc))
                continue
            else:
                break

        cctv_area_cnt[k] = cnt

    if no == 1:
        idx = cctv_area_cnt.index(max(cctv_area_cnt))
        for r, c in cctv_area[idx]:
            checked[r][c] = 1
    elif no == 2:
        if cctv_area_cnt[0] + cctv_area_cnt[2] >= cctv_area_cnt[1] + cctv_area_cnt[3]:
            for r, c in cctv_area[0]:
                checked[r][c] = 1
            for r, c in cctv_area[2]:
                checked[r][c] = 1
        else:
            for r, c in cctv_area[1]:
                checked[r][c] = 1
            for r, c in cctv_area[3]:
                checked[r][c] = 1
    elif no == 3:
        compare = [sum(cctv_area_cnt[0:2]), sum(cctv_area_cnt[1:3]), sum(cctv_area_cnt[2:4]), cctv_area_cnt[3] + cctv_area_cnt[0]]
        idx = compare.index(max(compare))
        for r, c in cctv_area[idx]:
            checked[r][c] = 1
        for r, c in cctv_area[(idx + 1) % 4]:
            checked[r][c] = 1
    elif no == 4:
        idx = cctv_area_cnt.index(min(cctv_area_cnt))
        for i in range(4):
            if i == idx:
                continue
            for r, c in cctv_area[i]:
                checked[r][c] = 1
    else:
        for i in range(4):
            for r, c in cctv_area[i]:
                checked[r][c] = 1


checked = [[0] * M for _ in range(N)]

for n in range(N):
    for m in range(M):
        if 1 <= cctv[n][m] <= 5:
            getCctvArea(n, m, cctv[n][m])

result = 0
for n in range(N):
    for m in range(M):
        if checked[n][m] == 0 and cctv[n][m] != 6:
            result += 1

print(result)