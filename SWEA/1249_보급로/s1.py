import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    land = [list(map(int, input())) for _ in range(N)]

    cost = [[987654321]*N for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # BFS
    que = [(0, 0)]
    cost[0][0] = 0

    while que:
        r, c = que.pop(0)

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                new_cost = cost[r][c] + land[nr][nc]
                if new_cost < cost[nr][nc]:
                    cost[nr][nc] = new_cost
                    que.append((nr, nc))

    print('#{} {}'.format(tc, cost[N-1][N-1]))

