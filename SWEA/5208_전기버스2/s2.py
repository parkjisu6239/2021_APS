import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, int(input())+1):
    temp = list(map(int, input().split()))
    N = temp[0]
    bus_stop = temp[1:]
    # 해당 정류장에 도달하는 최소거리 리스트
    d = [10000 for _ in range(N)]
    d[0] = -1
    for i in range(N - 1):
        power = bus_stop[i]
        for j in range(i + 1, i + 1 + power):
            d[j] = min(d[j], d[i] + 1)
            if j == N - 1:
                break

    print('#{} {}'.format(tc, d[N - 1]))