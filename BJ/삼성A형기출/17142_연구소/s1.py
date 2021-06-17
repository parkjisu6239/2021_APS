import sys
from itertools import combinations
sys.stdin = open('eval_input.txt')


def BFS(start): # 출발지가 여럿인 경우 BFS
    max_time = 0 # 감염 최대 시간
    empty = 0 # 빈칸인데 감염안된 곳 있는지 체크
    que = start # 조합 중에 한개
    visit = [[-1]*N for _ in range(N)] # 미방문지 -1 (거리라 0인 경우가 있어서)

    for x, y in que: # 활성 바이러스 위치 0
        visit[x][y] = 0

    while que:
        r, c = que.pop(0)
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if visit[nr][nc] == -1 and lab[nr][nc] != 1: # 방문하지 않았고, 벽이 아닌 경우
                    visit[nr][nc] = visit[r][c] + 1
                    if lab[nr][nc] == 0: # 0인 경우 빈칸 갯수 세기
                        empty += 1
                        max_time = max(visit[nr][nc], max_time) # 비활성 바이러스는 최대값 세지 않음
                    que.append((nr, nc))


    if empty == empty_total: # 빈칸 모두 채운경우
        return max_time
    else: # 감염안된 빈칸있는 경우
        return -1


## input ##
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
virus = []

empty_total = 0
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append((i, j))
        elif lab[i][j] == 0:
            empty_total += 1

## 활성바이러스 조합 ##
active_virus = list(map(list, combinations(virus, M)))

## 방향 델타 ##
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

## 최대시간 구하기 ##
min_time = 987654321
for active in active_virus:
    time = BFS(active)
    if time != -1:
        min_time = min(min_time, time)

## 다 -1 이어서 min_time이 갱신 안된 경우
if min_time == 987654321:
    min_time = -1

print(min_time)





