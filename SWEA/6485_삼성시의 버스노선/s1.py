import sys
sys.stdin = open("input.txt", "r")
'''
# 런타임 에러
T =int(input())
for tc in range(1, T+1):
    # 1. 입력받기
    # 1.1 노선의 갯수
    nosun_cnt = int(input())

    # 1.2 각 노선이 지나는 버스정류장 위치 정보
    # 각 노선의 버스가 지나는 정류장 정보
    # 버스는 각 요소의 0번 인덱스 ~ 1번 인덱스를 지남
    bus_nosun = [0] * nosun_cnt
    for i in range(nosun_cnt):
        bus_nosun[i] = list(map(int, input().split()))

    # 1.3 버스정류장의 갯수
    bus_stop_cnt = int(input())

    # 1.4 버스정류장 1~P
    # 밑에는 안받아도 되는데, 테스트 케이스 늘어나면 받아야되서 일단 받음
    bus_stop_location = []
    for _ in range(bus_stop_cnt):
        bus_stop_location.append(int(input()))

    # 여기까지 입력 받기 끝!

    # 값을 구해보자(각 인덱스의 정류장을 지나는 버스의 수)
    result = [0] * bus_stop_cnt

    for i in range(nosun_cnt):
        for j in range(bus_nosun[i][0]-1, bus_nosun[i][1]):
            result[j] += 1

    print('#{} {}'.format(tc, " ".join(list(map(str, result)))))
'''


#
T =int(input())
for tc in range(1, T+1):
    N = int(input())
    # 5000개의 버스가 있으니까 일단 만들어놓음
    bus_stop = [0] * 5001
    # 값을 받자마자 입력하게끔
    for i in range(N):
        # 노선이 지나는 정류장 시작~끝을 받음(예시에서 1,3)
        A, B = map(int, input().split())
        # A~B를 지나는 거니까 버정 수를 늘려줌
        for j in range(A, B+1):
            bus_stop[j] += 1

    # 다 늘려준 다음에 다음 값을 받음
    P = int(input())
    # 출력의 tc 번호를 뽑고, 한칸 띄워놓음
    print('#{}'.format(tc),end=' ')
    # p 만큼, p다음에 나오는 숫자를 입력받고, 그 인덱스에 맞는
    # bus_stop의 값을 출력함
    for i in range(P):
        C = int(input())
        print(bus_stop[C], end=" ")
    print()