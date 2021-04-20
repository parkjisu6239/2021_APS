import sys
sys.stdin = open('input.txt', 'r')


def change_battry(idx, battery, cnt):
    global min_cnt
    if idx == N-1:
        if cnt < min_cnt:
            min_cnt = cnt
        return

    if cnt > min_cnt:
        return

    if battery: # 배터리 있으면
        change_battry(idx+1, battery-1, cnt) # 충전 안해도 되고, 해도 되고
    change_battry(idx + 1, bus_stop[idx]-1, cnt + 1)  # 없으면 무조건 충전


for tc in range(1, int(input())+1):
    temp = list(map(int, input().split()))
    N = temp[0]
    bus_stop = temp[1:]
    min_cnt = 99999999
    change_battry(1, bus_stop[0]-1, 0)
    print('#{} {}'.format(tc, min_cnt))