import sys
sys.stdin = open('input.txt')

# 시작점이 무조건 맨밑인줄 알았는데 아니어따
def Find_start(N, maze):
    for r in range(1, N+1):
        for c in range(1, N+1):
            if maze[r][c] == 2:
                return [r, c]

# 미로 찾기
def MazeRunner(maze):
    # 출발점 찾아서 스택에 넣기
    global stack

    if not stack:
        return 0

    # 4방이동
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    # 현 위치를 스택에서 빼서, 방문체크
    r = stack[-1][0]
    c = stack[-1][1]
    stack.pop()
    maze[r][c] = 1

    # 현위치에서 갈 수 있는 좌표 스택에 쌓기
    for i in range(4):
        if maze[r+ dr[i]][c+ dc[i]] == 3:
            return 1
        elif maze[r+ dr[i]][c+ dc[i]] == 0:
            stack.append([r+ dr[i], c+ dc[i]])
            MazeRunner(maze)


for tc in range(1, int(input())+1):
    N = int(input())
    # 테두리 벽으로 두르기
    maze = [[1] * (N+2)]
    for _ in range(N):
        maze.append( [1] + list(map(int, input())) + [1])
    maze.append([1] * (N+2))
    stack = [Find_start(N, maze)]
    print('#{} {}'.format(tc, MazeRunner(maze)))