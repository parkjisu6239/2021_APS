from collections import deque
import sys
sys.stdin = open('input.txt')


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    # 물이 있는 곳을 찾자! 그곳들은 모두 BFS의 출발지가 된다.
    que = []
    # 방문체크와 물/땅을 한번에 저장하기 위해 땅은 -1, 밑에서 물은 0으로 변경
    arr = [[-1] * M for _ in range(N)]
    # 모든 거리들의 합
    diatance = 0

    # 인풋 저장, 물 좌표 큐에 쌓기, 방문체크
    for i in range(N):
        row = list(input())
        for j in range(M):
            if row[j] == 'W':
                arr[i][j] = 0
                que.append((i, j))

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 라이브러리 안쓰고 그냥 큐로 하면 시간초과
    que = deque(que)
    while que:
        i, j = que.popleft()

        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            # 인덱스 안넘고, 방문하지 않았다면, 땅이라면
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == -1:
                # 거리 저장
                arr[nr][nc] = arr[i][j] + 1
                diatance += arr[nr][nc]
                que.append((nr, nc))

    print('#{} {}'.format(tc, diatance))