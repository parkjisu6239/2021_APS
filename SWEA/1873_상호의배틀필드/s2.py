import sys
from pandas import DataFrame as df
sys.stdin = open('input.txt')


def BattleFeild(H, W, feild, action_cnt, action):
    # 아래 4개 리스트 상하좌우로 모두 인덱스 통일
    start = ['^', 'v', '<', '>']
    action_list = ['U', 'D', 'L', 'R']
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    #print(df(feild))
    # tank의 정보 초기화 (행위치, 열위치, 방향)
    tank = [-1, -1, '']

    # tank의 시작점 찾기
    for r in range(H):
        for c in range(W):
            # 이동 방향을 아직 찾지 못한 경우(초기값이 그대로 들어있는 경우)
            for j in range(len(start)):
                if feild[r][c] == start[j]:
                    tank[0] = r
                    tank[1] = c
                    tank[2] = start[j]
                    break
            if tank[0] != -1:
                break
        if tank[0] != -1:
            break

    #print(tank)

    # 입력 순서 만큼 반복
    for k in range(action_cnt):
        # go
        if action[k] != 'S':
            # 이동 방향 찾기
            for l in range(len(action_list)):
                # 이동했을 때 맵을 넘어가지 않으면
                if action[k] == action_list[l] and 0 <= tank[0] + dx[l] < H and 0 <= tank[1] + dy[l] < W:
                    # 평지이면, 방향 바꾸고 이동도 하기
                    if feild[tank[0] + dx[l]][tank[1] + dy[l]] == '.':
                        feild[tank[0]][tank[1]] = '.'  # 지금 있는 자리는 '.'으로 바꿔주기
                        # 탱크 정보 update
                        tank[2] = start[l]  # 방향 전환 : '^', 'v', '<', '>' 중 1
                        tank[0] += dx[l]  # 위치 전환 : x
                        tank[1] += dy[l]  # 위치 전환 : y
                        # 새로운 탱크정보로 이동하기
                        feild[tank[0]][tank[1]] = tank[2]  # 이동하기
                    # 물이거나 벽이면 방향전환만 하기
                    else:
                        tank[2] = start[l]  # 방향 전환 : '^', 'v', '<', '>' 중 1
                        feild[tank[0]][tank[1]] = tank[2]
                # 인덱스가 넘어가는 경우, 방향 전환만
                elif action[k] == action_list[l]:
                    tank[2] = start[l]  # 방향 전환 : '^', 'v', '<', '>' 중 1
                    feild[tank[0]][tank[1]] = tank[2]
        # shoot
        else:
            # 방향 찾기
            for m in range(len(start)):
                if tank[2] == start[m]:
                    # 이동 방향을 찾았다면 그쪽으로 총알을 쏘기
                    # 인덱스를 넘지 않을 때까지 반복 (총알의 이동!)
                    n = 1
                    while 0 <= tank[0] + n * dx[m] < H and 0 <= tank[1] + n * dy[m] < W:
                        # 한칸 이동 시 강철벽이 있다면
                        if feild[tank[0] + n * dx[m]][tank[1] + n * dy[m]] == '#':
                            # 아무일도 없고 종료
                            break
                        # 한칸 이동 시 벽돌벽이 있다면
                        elif feild[tank[0] + n * dx[m]][tank[1] + n * dy[m]] == '*':
                            # 벽 부시고 종료
                            feild[tank[0] + n * dx[m]][tank[1] + n * dy[m]] = '.'
                            break
                        # 물이거나 평지이면 한칸 더 이동
                        else:
                            n += 1

    for f in feild:
        print(''.join(map(str, f)))


for tc in range(1, int(input()) + 1):
    H, W = map(int, input().split())
    feild = [list(input()) for _ in range(H)]
    action_cnt = int(input())
    action = list(input())
    print('#{}'.format(tc), end=' ')
    BattleFeild(H, W, feild, action_cnt, action)