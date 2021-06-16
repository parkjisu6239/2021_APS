import sys
sys.stdin = open('input.txt', 'r')
q = lambda: map(int, sys.stdin.readline().split())

N, M, r, c, K = q()
arr = [list(q()) for _ in range(N)]
cmd = list(q())

move = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

dice = [0] * 6 # 위, 앞, 밑, 뒤, 좌, 우

# 남쪽 회전 -> 뒤, 위, 앞, 밑, 좌, 우
# 북쪽 회전 -> 앞, 밑, 뒤, 위, 좌, 우
# 서쪽 회전 -> 우, 앞, 좌, 뒤, 위, 밑
# 동쪽 회전 -> 좌, 앞, 우, 뒤, 밑, 위

for k in range(K):
    go = cmd[k]
    dr, dc = move[go]
    nr, nc = r + dr, c + dc

    if not (0 <= nr < N and 0 <= nc < M):
        continue

    r, c = nr, nc
    up, front, down, back, left, right = dice

    # 회전
    if go == 4:
        dice[0], dice[1], dice[2], dice[3] = back, up, front, down
    elif go == 3:
        dice[0], dice[1], dice[2], dice[3] = front, down, back, up
    elif go == 2:
        dice[0], dice[2], dice[4], dice[5] = right, left, up, down
    elif go == 1:
        dice[0], dice[2], dice[4], dice[5] = left, right, down, up

    # 복사
    if arr[r][c] == 0:
        arr[r][c] = dice[2]
    else:
        dice[2] = arr[r][c]
        arr[r][c] = 0

    print(dice[0])
