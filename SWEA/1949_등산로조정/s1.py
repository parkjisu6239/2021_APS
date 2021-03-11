import sys
sys.stdin = open("input.txt", "r")

def DFS(i, j, work, length):
    global max_len

    # 방문체크
    visited[i][j] = 1

    for k in range(4):
        nr = i + dr[k]
        nc = j + dc[k]
        # 인덱스 안넘고, 방문하지 않은 곳 중에
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            # 현재 높이보다 낮으면 ㄱㄱ
            if jido[nr][nc] < jido[i][j]:
                stack.append([nr, nc])
                DFS(*stack.pop(), work, length + 1)
            # 현재 높이보다 높지만
            else:
                # 공사안했고, 공사해서 갈 수 있으면 ㄱㄱ
                if work and jido[nr][nc] - jido[i][j] < K :
                    # 공사해야하는 높이
                    work_len = jido[nr][nc] - jido[i][j] + 1
                    # 공사하기
                    jido[nr][nc] -= work_len
                    # 갈 수 있는 곳으로 추가
                    stack.append([nr, nc])
                    # 공사 체크
                    work = 0
                    # ㄱㄱ
                    DFS(*stack.pop(), work, length + 1)

                    # 다시 나왔을 때는 높이 복구, 공사 복구
                    jido[nr][nc] += work_len
                    work = 1

    # 4방향 다 봤는데, 갈데가 없어서 여기로 오게 된것임!
    # 그럼 되돌아 가야하니까, 방문체크 빼주고, 지금까지 구한 거리를 갱신
    visited[i][j] = 0
    if length > max_len:
        max_len = length


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())

    # 지도 저장 & 최고 높이 구하기
    jido = []
    jido_high = 0
    for _ in range(N):
        jido_row = list(map(int, input().split()))
        jido.append(jido_row)
        if max(jido_row) > jido_high:
            jido_high = max(jido_row)

    # 방문체크, 상하좌우
    visited = [[0 for _ in range(N)] for _ in range(N)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    max_len = 0
    for i in range(N):
        for j in range(N):
            if jido[i][j] == jido_high:
                # 현위치, 공사여부, 등산로 길이
                stack = [[i, j]]
                visited[i][j] = 1
                DFS(i, j, 1, 1)

    print('#{} {}'.format(tc, max_len))