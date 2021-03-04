import sys
sys.stdin = open('input.txt')

# BFS 재귀
def Find_start(N, maze):
    for r in range(1, N+1):
        for c in range(1, N+1):
            if maze[r][c] == 2:
                return [r, c]

# 미로 찾기
def MazeRunner_BFS_re(Q):
    global result

    if not Q:
        return
    else:
        r, c = Q.pop(0)

        if maze[r][c] == 3:  # base case
            result = 1
            return

        # 4방이동
        dr = [1, -1, 0, 0]
        dc = [0, 0, -1, 1]

        # 현 위치를 스택에서 빼서, 방문체크
        maze[r][c] = 1

        # 현위치에서 갈 수 있는 좌표 스택에 쌓기
        for i in range(4):
            if maze[r + dr[i]][c + dc[i]] == 0 or maze[r + dr[i]][c + dc[i]] == 3:
                Q.append([r + dr[i], c + dc[i]])
        MazeRunner_BFS_re(Q)


for tc in range(1, int(input())+1):
    N = int(input())
    # 테두리 벽으로 두르기
    maze = [[1] * (N+2)]
    for _ in range(N):
        maze.append( [1] + list(map(int, input())) + [1])
    maze.append([1] * (N+2))

    result = 0
    Q = [Find_start(N, maze)]
    MazeRunner_BFS_re(Q)
    print('#{} {}'.format(tc, result))