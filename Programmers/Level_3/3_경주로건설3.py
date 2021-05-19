def solution(board):
    N = len(board)
    cost = [[987654321] * N for _ in range(N)]
    start = (0, 0, 0)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    que = [start]
    cost[0][0] = 0

    while que:
        r, c, direction = que.pop()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0:
                if (r, c) == (0, 0) or direction == k:
                    if cost[r][c]+100 <= cost[nr][nc]:
                        que.append((nr, nc, k))
                        cost[nr][nc] = cost[r][c]+100
                else:
                    if cost[r][c]+600 <= cost[nr][nc]:
                        que.append((nr, nc, k))
                        cost[nr][nc] = cost[r][c]+600

    return cost[N-1][N-1]

# print(solution([[0,0,0],[0,0,0],[0,0,0]]), 900)
# print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]), 3800)
# print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]), 2100)
print(solution([[0,0,0,0,0,0],
                [0,1,1,1,0,0],
                [0,0,1,0,0,0],
                [1,0,0,1,0,1],
                [1,1,0,0,0,1],
                [1,0,1,0,0,0]]))
