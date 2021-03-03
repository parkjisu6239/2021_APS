import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    D, A, B, F = map(int, input().split())

    # 속력! 시간이 필요
    # 기차사이의 거리 = D - (A + B)*t
    # 그 안에서 파리가 왔다갔다 한다.
    # 파리가 기차에 닿았다는 것을 어떻게 확인? 기차전면부의 위치 필요!

    # 초기 기차 머리 위치(수직선위)
    A_head = 0
    B_head = D

    # 파리의 이동거리, 현위치
    fly_distance = 0
    fly_location = 0

    # 경과시간
    time = 0

    # 방향 정방향(A>B) 역방향(B>A)
    direction = True

    # 기차가 부딛히기 전까지 (파리가 죽기 전까지)
    while A_head != B_head:
        # 1시간 경과
        time += 1

        # 기차와 파리의 위치와 이동거리 기록
        A_head += A
        B_head -= B
        if direction:
            fly_location += F
        else:
            fly_location -= F
        fly_distance += F

        # 파리가 기차와 만났다면, 파리의 이동방향 전환
        if fly_distance == B_head:
            direction = False
        elif fly_distance == A_head:
            direction = True

    # 파리가 죽었으면 그동안 이동한 거리 출력
    print('#{} {}'.format(tc, fly_distance))
