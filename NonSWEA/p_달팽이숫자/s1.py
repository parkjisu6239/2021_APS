import sys
sys.stdin = open("input.txt", "r")

def snail(N):
    # N * N 행렬의 모든 원소를 0으로 초기화
    snail_list = [[0 for _ in range(N)] for _ in range(N)]

    # 우 > 하 > 좌 > 상 (시계방향, 달팽이 껍질 모양)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # 처음 시작인덱스는 고정, 그 위치의 값도 1로 고정
    # 반복문에 들어가면 인덱스에 계속 dx,dy가 더해질 거라, 밖에서 수행함
    x, y = 0, 0
    snail_list[0][0] = 1

    # 이동방향 초기화, 위에서 1은 넣었으니까 2 ~ N**2까지 리스트에 담을 것
    k = 0
    i = 2
    while i <= N**2:
        # 1. 이 조건문은 1회 반복시 1.1~1.3 중에 한개만 수행함
        # 1.2.
        # 만약 현재 진행방향으로 이동했을때, 인덱스를 넘어가면
        # K에 1을 더하여 진행방향을 바꿈 (우 > 하 > 좌 > 상 순서로 변경됨)
        if x + dx[k] >= N or y + dy[k] >= N or x + dx[k] < 0 or y + dy[k] < 0:
            k += 1
        # 1.3.
        # 만약 진행방향으로 이동했을때 인덱스를 넘지는 않지만,
        # 이동한 인덱스에 이미 0이 아닌 값이 있으면 이전 반복에서 값이 할당되었으므로
        # 진행 방향을 변경함
        elif snail_list[x + dx[k]][y + dy[k]] :
            k += 1
        # 1.1.
        # 현위치에서 한칸 진행방향으로 이동한 위치에 i를 할당함
        # i 할당이 완료 될 경우, 다음 i를 위해 값을 1 올려줌
        else:
            x = x + dx[k]
            y = y + dy[k]
            snail_list[x][y] = i
            i += 1

        # 2. 이 조건문은 반복시 무조건 수행됨
        # 만약 진행방향을 계속 바꾸다가, K가 4이상이되면
        # 4를 빼서 다시 0부터 시작하게 함
        if k >= 4:
            k -= 4

    for escargo in snail_list:
        print(*escargo)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc))
    snail(N)