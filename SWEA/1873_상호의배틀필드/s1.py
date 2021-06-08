import sys
sys.stdin = open('eval_input.txt')


def Findstart(feild):
    start = ['^', 'v', '<', '>']
    tank = []

    for r in range(W):
        for c in range(H):
            if feild[r][c] in start:
                tank.append(r)
                tank.append(c)
                tank.append(feild[r][c])
                return tank

def Go(action, feild, tank):
    start = ['^', 'v', '<', '>']
    action_list = ['U', 'D', 'L', 'R']
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    direction = action_list.index(action)
    nx = tank[0] + dx[direction]
    ny = tank[1] + dy[direction]
    if 0 <= nx < H and 0 <= ny < W:
        if feild[nx][ny] == '.':
            feild[tank[0]][tank[1]] = '.'  # 지금 있는 자리는 '.'으로 바꿔주기
            # 탱크 정보 update
            tank[2] = start[direction]  # 방향 전환 : '^', 'v', '<', '>' 중 1
            tank[0] += dx[direction]  # 위치 전환 : x
            tank[1] += dy[direction]  # 위치 전환 : y
            # 새로운 탱크정보로 이동하기
            feild[tank[0]][tank[1]] = tank[2]  # 이동하기
        else:
            tank[2] = start[direction]  # 방향 전환 : '^', 'v', '<', '>' 중 1
            feild[tank[0]][tank[1]] = tank[2]
            # 인덱스가 넘어가는 경우, 방향 전환만
    elif action[k] == action_list[l]:
        tank[2] = start[l]  # 방향 전환 : '^', 'v', '<', '>' 중 1
        feild[tank[0]][tank[1]] = tank[2]

def Shoot(feild, tank):
    start = ['^', 'v', '<', '>']
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    direction = start.index(tank[2])
    n = 1
    while 0 <= tank[0] + n * dx[direction] < H and 0 <= tank[1] + n * dy[direction] < W:
        # 한칸 이동 시 강철벽이 있다면
        if feild[tank[0] + n * dx[direction]][tank[1] + n * dy[direction]] == '#':
            # 아무일도 없고 종료
            break
        # 한칸 이동 시 벽돌벽이 있다면
        elif feild[tank[0] + n * dx[direction]][tank[1] + n * dy[direction]] == '*':
            # 벽 부시고 종료
            feild[tank[0] + n * dx[direction]][tank[1] + n * dy[direction]] = '.'
            break
        # 물이거나 평지이면 한칸 더 이동
        else:
            n += 1


def BattleFeild(H, W, feild, action_cnt, action):
    # 아래 4개 리스트 상하좌우로 모두 인덱스 통일
    start = ['^', 'v', '<', '>']
    action_list = ['U', 'D', 'L', 'R']
    dx = [-1, 1, 0 , 0]
    dy = [0 , 0, -1, 1]

    # tank의 정보
    tank = Findstart(feild)

    # 입력 순서 만큼 반복
    for k in range(action_cnt):
        # go
        if action[k] != 'S':
            Go(action[k], feild, tank)
        # shoot
        else:
            Shoot(feild, tank)

    for f in feild:
        print(''.join(map(str, f)))


for tc in range(1, int(input())+1):
    H, W = map(int, input().split())
    feild = [ list(input()) for _ in range(H) ]
    action_cnt = int(input())
    action = list(input())
    print('#{}'.format(tc), end=' ')
    BattleFeild(H, W, feild, action_cnt, action)
