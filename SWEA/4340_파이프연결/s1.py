import sys
sys.stdin = open('input.txt')
import time
start = time.time()

# 상 우 하 좌 = 1, 2, 3, 4 (이전 파이프와의 연결 방향)
def dfs(r, c, cnt, connect_direction):
    global Min

    if (r, c) == (N-1, N-1): # 도착하면 최소값 갱신
        # 마지막 파이프가 직선인 경우, 반드시 왼쪽 연결
        if pipes[r][c] in (1, 2) and connect_direction == 4:
            Min = min(Min, cnt)
        # 마지막 파이프가 직선인 경우, 반드시 위쪽 연결
        elif pipes[r][c] in (3, 4, 5, 6) and connect_direction == 1:
            Min = min(Min, cnt)
        return

    if cnt > Min:
        return

    if visit[r][c]:
        return

    visit[r][c] = 1

    for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = r + x, c + y
        if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visit and pipes[nr][nc]: # 경계 안넘고, 방문하지 않은 곳
            # 현위치의 파이프가 직선 모양인지, 곡선모양인지에 따라 선택지가 다르다.
            if pipes[r][c] in (1, 2): # 직선 모양이고
                if connect_direction in (1, 3): # 이전 파이프와 상or하로 연결되어 있으면
                    # 2번 모양만 가능 => nr, nc가 상 or 하 여야한다.
                    if (x, y) == (-1, 0):
                        dfs(nr, nc, cnt+1, 3)
                    elif (x, y) == (1, 0):
                        dfs(nr, nc, cnt + 1, 1)
                else: # 이전 파이프와 좌or우로 연결되어 있으면
                    # 1번 모양만 가능 => nr, nc가 좌 or 우 여야한다.
                    if (x, y) == (0, -1):
                        dfs(nr, nc, cnt+1, 2)
                    elif (x, y) == (0, 1):
                        dfs(nr, nc, cnt + 1, 4)

            else: # 곡선 파이프
                if connect_direction == 1:
                    # 5번으로 연결
                    if (x, y) == (0, -1):
                        dfs(nr, nc, cnt+1, 2)
                    # 6번으로 연결
                    elif (x, y) == (0, 1):
                        dfs(nr, nc, cnt + 1, 4)
                elif connect_direction == 2:
                    # 3번으로 연결
                    if (x, y) == (1, 0):
                        dfs(nr, nc, cnt + 1, 1)
                    # 6번으로 연결
                    elif (x, y) == (-1, 0):
                        dfs(nr, nc, cnt+1, 3)
                elif connect_direction == 3:
                    # 3번으로 연결
                    if (x, y) == (0, 1):
                        dfs(nr, nc, cnt + 1, 4)
                    # 4번으로 연결
                    elif (x, y) == (0, -1):
                        dfs(nr, nc, cnt+1, 2)
                else:
                    # 4번으로 연결
                    if (x, y) == (1, 0):
                        dfs(nr, nc, cnt + 1, 1)
                    # 5번으로 연결
                    elif (x, y) == (-1, 0):
                        dfs(nr, nc, cnt+1, 3)

    visit[r][c] = 0



for tc in range(1, int(input())+1):
    N = int(input())
    pipes = [list(map(int, input().split())) for _ in range(N)]

    # 현재 위치에서 파이프를 회전할 수 있다. 단, 이전 파이프와 연결되어야 한다.
    Min = 999999
    visit = [[0] * N for _ in range(N)]
    visit[0][0] = 1

    dfs(0, 1, 2, 4)

    print('#{} {}'.format(tc, Min))

print((time.time() - start))