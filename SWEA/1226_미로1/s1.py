import sys
sys.stdin = open('input.txt')

# 16*16 행렬 / 시작점은 (1, 1) / 도착점은 (13, 13) > 도달 가능 1/ 불가 0
def MazeRunner(que, maze):
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0 , -1, 1]

    # que가 빌 때까지
    while que:
        # 맨앞에 있는 정점
        r, c = que.pop(0)

        # 4방 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr == nc == 13:
                return 1

            # 벽이 아니고, 방문하지 않았다면 que에 넣자
            if maze[nr][nc] != 1:
                # 인접정점을 큐에 넣고, 방문표시
                que.append([nr, nc])
                maze[nr][nc] = 1

    return 0


for _ in range(1, 11):
    tc = int(input())
    maze = [ list(map(int, input())) for _ in range(16)]

    # 시점
    que = [[1, 1]]

    # 출력
    print('#{} {}'.format(tc, MazeRunner(que, maze)))


