import sys
sys.stdin = open('input.txt')


for _ in range(1, 11):
    # 사다리는 100*100
    # 인덱스 에러 생각 안하기 위해 좌우 0 쿠션 만들기
    tc = int(input())
    sadary = [ [0] + list(map(int, input().split())) + [0]  for _ in range(100)]
    #print(sadary)

    # 모든 출발점 찾기
    start = []
    for i in range(102):
        if sadary[0][i] == 1:
            start.append(i)

    # 앞뒤로 쿠션놔서 실제 출력해야하는 시작 인덱스보다 1씩 크기때문에
    # 최종 출력할때 -1 해줘야함
    #print(start)

    # 방향 델타 (사다리 위 > 아래) 하, 좌, 우
    dx = [1, 0, 0]
    dy = [0, -1, 1]

    distance = [0] * len(start)

    for i in range(len(start)):
        # 시작점, 방향 초기화
        x = 0
        y = start[i]
        k = 1

        while x < 100: # 바닥에 닿을 때 까지
            # 이동방향이 왼쪽/오른쪽이고
            if k != 0:
                # 그쪽으로 더 갈 수 있으면
                if sadary[x + dx[k]][y + dy[k]] == 1:
                    # 더 가라
                    x += dx[k]
                    y += dy[k]
                    distance[i] += 1
                # 더 갈수 없으면
                else:
                    # 아래로 꺽어라
                    k = 0
                    x += dx[k]
                    y += dy[k]
                    distance[i] += 1
            # 이동 방향이 아래쪽이고
            else:
                # 왼쪽으로 갈 수 있으면
                if sadary[x + dx[1]][y + dy[1]] == 1:
                    # 왼쪽으로 꺽어라
                    k = 1
                    x += dx[k]
                    y += dy[k]
                    distance[i] += 1
                # 오른쪽으로 갈 수 있으면
                elif sadary[x + dx[2]][y + dy[2]] == 1:
                    # 오른쪽으로 꺽어라
                    k = 2
                    x += dx[k]
                    y += dy[k]
                    distance[i] += 1
                # 왼오 둘다 못가면
                else:
                    # 아래로 가라
                    x += dx[k]
                    y += dy[k]
                    distance[i] += 1

    #print(distance)

    # 최소값이 복수개인 경우 가장큰 x 좌표!
    min_idx = 0
    for i in range(len(distance)):
        if distance[i] <= distance[min_idx]:
            min_idx = i

    print('#{} {}'.format(tc, start[min_idx]-1))


