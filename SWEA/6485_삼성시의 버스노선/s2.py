import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    # 버정 수는 5000개지만, 1부터 시작하고, 인덱스는 0부터 시작하기 때문에 5001개를 만들어줌(인덱스 0~5000)
    bus_stop = [0] * 5001

    # 노선의 갯수를 받음
    N = int(input())

    # 입력받은 노선 수만큼 반복
    for _ in range(N):
        # 시점, 종점
        nosun_start, nosun_end = map(int, input().split())
        # 시점~종점이 지나는 버정수를 더해줌
        for nosun in range(nosun_start, nosun_end+1):
            bus_stop[nosun] += 1

    # 알고싶은 버정의 1~p까지 번호
    P = int(input())

    print('#{}'.format(tc), end = " ")
    for _ in range(P):
        print(bus_stop[int(input())], end=" ")
    print()