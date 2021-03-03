import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input())+1):
    # N : 파리들이 있는 방바닥 길이, M : 파리채 길이 > 둘다 정사각형
    N, M = map(int, input().split())
    fly = []

    # 파리 넣기
    for _ in range(N):
        fly.append(list(map(int, input().split())))
    
    # 최대로 죽일 수 있는 파리수 
    max_fly = 0
    # 0 ~ N-M까지만 때려도 파리채 길이가 M이라 다 때려짐 (행렬 마찬가지)
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # 파리채로 잡을 수 있는 파리 수
            local_fly = 0
            # 파리채의 길이만큼
            for k in range(M):
                for l in range(M):
                    # 행열에 인덱스를 더해주면 정해진 위치를 때렸을때 잡을 수 있는
                    # 파리들의 수를 구할 수 있음
                    local_fly += fly[i+k][j+l]
            # 그때 때린 파리가 최대이면 최대로 지정
            if max_fly < local_fly:
                max_fly = local_fly

    print('#{} {}'.format(tc, max_fly))
