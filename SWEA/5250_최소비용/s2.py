import sys
sys.stdin = open('input.txt')


def BFS():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visit = [[987654321]*N for _ in range(N)]

    visit[0][0] = 0
    que = [(0, 0)]

    while que:
        r, c = que.pop(0)

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
               if max(land[nr][nc]-land[r][c], 0) + visit[r][c] + 1 < visit[nr][nc]:
                   visit[nr][nc] = max(land[nr][nc]-land[r][c], 0) + visit[r][c] + 1
                   que.append((nr, nc))

    return visit



for tc in range(1, int(input())+1):
    N = int(input())
    land = [list(map(int, input().split())) for _ in range(N)]
    result = BFS()
    print('#{} {}'.format(tc, result[N-1][N-1]))


