import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [ list(input()) for _ in range(N) ]
    distance = [ [0]*M for _ in range(N) ]

    #WLL
    #LLL
    # 여기서 1행 2열 L은 저 8방향 확인으로 W에 도달할 수 없다.
    # 땅을 기준이 아니라 물을 기준으로 나와 땅의 거리를 계산?
    # 쿠션 필요 X, 주어진 N*M 크기의 0으로만 채워진 가상 공간을 만든다
    # 전체 행렬을 순회하면서 물을 찾는다, 그 물로부터 땅까지의 거리를 모두 가상 공간에 저장한다.
    # 또 다른 물이 나온다면, 앞서 작성한 거리보다 가까운 경우에 그 값을 변경하고, 그렇지 않아면 저장하지 않는다.
    # 모든 반복을 끝내고 나면, 각자 가장 가까운 거리의 물과 거리가 저장되어있다. 그때 모든 행렬을 값을 더하면 된다.
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                for k in range(N):
                    for l in range(M):
                        if arr[k][l] == 'L' and distance[k][l] != 1:
                            # 거리가 비어있으면 그냥 바로 넣고
                            if distance[k][l] == 0:
                                distance[k][l] = abs(i-k) + abs(j-l)
                            else: # 거리가 이미 지정되어있으면
                                # 새로운 거리가 이미 지정된 거리보다 작을 때만 업데이트
                                if abs(i-k) + abs(j-l) < distance[k][l]:
                                    distance[k][l] = abs(i - k) + abs(j - l)

    result = 0
    for r in distance:
        result += sum(r)

    print('#{} {}'.format(tc, result))



