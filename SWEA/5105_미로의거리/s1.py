import sys
sys.stdin = open('input.txt')

def MazeRunner(que, maze):
    # visited 없이 지나온 길을 시점과의 거리로 바꿔줄 것이다.
    # 그런데 시점과의 거리가 2, 3인 경우에는 이게 종점인지, 거리인지 알 수 없다.
    # 그래서 거리는 음수로 넣고 출력할때 - 붙여서 출력한다.
    distance = -1

    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0 , -1, 1]

    # que가 빌 때까지
    while que:
        # 맨앞에 있는 정점
        r, c = que[0][0], que[0][1]
        que.pop(0)

        # 4방 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 벽이 아니고, 방문하지 않았다면 que에 넣자
            if maze[nr][nc] != 1 and maze[nr][nc] >= 0:
                # 한칸 더 가면 목적지인 경우
                if maze[nr][nc] == 3:
                    # 현위치 거리에서 한칸 더 간게 시점~ 종점 거리니까 +1 하고 절대값
                    return -(distance + 1)
                # 목적지 아닌 경우
                else:
                    # 인접정점을 큐에 넣고, 방문표시를 시점과의 거리로 (음수로)
                    que.append([nr, nc])
                    maze[nr][nc] = distance

        # 동일거리의 인접 노드가 큐에서 다 빠진 경우에 거리 +1
        if que and maze[r][c] != maze[que[0][0]][que[0][1]]:
            distance -= 1

    return 0

# 시점 찾기
def Find_Start(maze):
    for i in range(1, N+2):
        for j in range(1, N+2):
            if maze[i][j] == 2:
                return i, j

# 최단거리 구하기
for tc in range(1, int(input())+1):
    N = int(input())

    # 테두리에 벽 놓기
    maze = [[1] * (N+2)]
    for _ in range(N):
        maze.append( [1] + list(map(int, input())) + [1] )
    maze.append([1] * (N + 2))

    # 시점
    r, c = Find_Start(maze)
    que = [[r, c]]

    # 출력
    print('#{} {}'.format(tc, MazeRunner(que, maze)))


