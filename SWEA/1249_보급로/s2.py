import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    land = [list(map(int, input())) for _ in range(N)]

    cost = [[987654321]*N for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    que = []
    heappush(que, (0, 0, 0)) # 비용, x좌표, y좌표
    cost[0][0] = 0

    while cost[N-1][N-1] == 987654321:
        w, r, c = heappop(que)

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                new_w = w + land[nr][nc]
                if new_w < cost[nr][nc]:
                    cost[nr][nc] = new_w
                    heappush(que, (new_w, nr, nc))

    print('#{} {}'.format(tc, cost[N-1][N-1]))

