dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solution(maps):
    r = len(maps)
    c = len(maps[0])
    visit = [[0] * c for _ in range(r)]
    answer = 0

    def get_len(x, y):
        land_len = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] == 1:
                continue
            else:
                land_len += 1
        return land_len

    def bfs(i, j):
        nonlocal answer
        que = [(i, j)]
        island_len = 0

        while que:
            x, y = que.pop(0)

            island_len += get_len(x, y)

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] == 1 and visit[nx][ny] == 0:
                    que.append((nx, ny))
                    visit[nx][ny] = 1

        answer = max(answer, island_len)

    for i in range(r):
        for j in range(c):
            if visit[i][j] == 0 and maps[i][j] == 1:  # 방문 안한 섬
                visit[i][j] = 1
                bfs(i, j)

    return answer


print(solution([[0,0,1,0,0],[0,1,1,0,1],[0,0,1,0,1],[1,1,1,0,1]]))