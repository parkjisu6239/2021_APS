import sys
sys.stdin = open("input2.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [ list(map(int, input().split())) for _ in range(N) ]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 1. 가장자리 제외
    print('가장자리 제외')
    # 가장자리는 행렬의 맨앞,맨끝인덱스
    # 원래 인덱스는 0~4이므로, 가장자리 제거이면 1~3
    abs_sum = 0
    for i in range(1, N-1):
        for j in range(1, N-1):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dx[k]
                abs_sum += abs(matrix[nx][ny] - matrix[i][j])
    print(abs_sum)

    # 2. 가장자리를 포함하여 계산
    print('가장자리를 포함하여 계산')
    abs_sum = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                # 벽에 닿으면 더하지 않기
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                abs_sum += abs(matrix[nx][ny] - matrix[i][j])
    print(abs_sum)