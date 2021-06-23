import sys
sys.stdin = open('input.txt')
q = lambda: map(int, sys.stdin.readline().split())

N, M = q()
cctv = [list(q()) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def getCctvArea(r, c, no):
    cctv_area = [{(r, c)} for _ in range(4)]

    for k in range(4):
        nr, nc = r, c

        while True:
            nr += dr[k]
            nc += dc[k]
            if 0 <= nr < N and 0 <= nc < M and (not cctv[nr][nc] == 6):
                cctv_area[k].add((nr, nc))
                continue
            else:
                break

    if no == 1:
        all_CCTV.append(cctv_area)
    elif no == 2:
        temp = [cctv_area[0]|cctv_area[2], cctv_area[1] | cctv_area[3]]
        all_CCTV.append(temp)
    elif no == 3:
        temp = [cctv_area[0]|cctv_area[1], cctv_area[1] | cctv_area[2], cctv_area[2] | cctv_area[3], cctv_area[3] | cctv_area[0]]
        all_CCTV.append(temp)
    elif no == 4:
        temp = [cctv_area[0] | cctv_area[1] | cctv_area[2],
                cctv_area[1] | cctv_area[2] | cctv_area[3],
                cctv_area[2] | cctv_area[3] | cctv_area[0],
                cctv_area[3] | cctv_area[0]| cctv_area[1]]
        all_CCTV.append(temp)
    else:
        all_CCTV.append(cctv_area[0] | cctv_area[1] | cctv_area[2] | cctv_area[3])


def dfs(n, union_set):
    global MAX
    if n==len(all_CCTV):
        if MAX < len(union_set):
            MAX = len(union_set)
        return
    for i in all_CCTV[n]:
        dfs(n+1, union_set|i)


checked = [[0] * M for _ in range(N)]

all_CCTV = []
empty = 0

for n in range(N):
    for m in range(M):
        if 1 <= cctv[n][m] <= 5:
            getCctvArea(n, m, cctv[n][m])
        if cctv[n][m] == 0:
            empty += 1


MAX = 0
dfs(0, set())

print(empty - MAX)