import sys
sys.stdin = open("input.txt", "r")
'''
def charge(bus_info, charge_machine):

    go = bus_info[0]
    end = bus_info[1]
    charge_machine_cnt = bus_info[2]

    # 만약 모든 충전기 사이의 거리가 go보다 작으면 일단 도착은 가능함
    # 충전기 사이가 go 보다 멀어서 도착 못하는 경우는 바로 0 리턴으로 종료
    for i in range(charge_machine_cnt-1):
        if go < charge_machine[i+1] - charge_machine[i]:
            return 0

    # 일단 갈수있는 만큼 가고 내 현위치부터, 지나온 길에 충전소가 있으면 거기서 충전!
    cnt = 0
    location = 0
    # 현위치가 end가 아니면 반복
    while location < end:
        # 내가 갈수 있는 최대만큼 가기
        location += go
        # 그리고 지금 내 위치, 내가 지나온 길에 충전소가 있는지 확인
        for j in range(location, -1, -1):
            # 최대만큼 갔을때 벌써 종점 도착하면 끝내기
            if location >= end:
                return cnt
            # 내 위치~지나온길에 충전기가 있으면
            # 충전기의 위치로 가기
            # 만약 내가 최대로 갔는데 우연히 거기에 충전기 있으면 그냥 끝
            # 근데 그 위치에 충전기 없으면 한개 뒤로, 또 뒤로 가면서 충전기 위치로 가기
            if j in charge_machine:
                location = j
                # 충전횟수 올리기
                cnt += 1
                break



T = int(input())
for tc in range(1, T+1):
    bus_info = list(map(int, input().split()))
    charge_machine = list(map(int, input().split()))
    print('#{} {}'.format(tc, charge(bus_info, charge_machine)))
'''


# 교수님 풀이
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # 충전기 설치 위치
    chargers = list(map(int, input().split()))
    stations = [True if n in chargers else False for n in range(N+1)]

    # 총 충전횟수 / 마지막 충전 위치에 대한 인덱스를 초기화
    charge_count = last_charge = 0

    # 시작과 동시에 현위치를 갱신하고 가자! > 갈수있는 만큼 최대로 가기
    current = K

    # 종점에 도착하지 않으면 반복
    while current < N:
        #3. 내가 마지막으로 충전한 위치가 지금 위치인가?
        # 앞으로 갔다 충전소가 없어서 계속 뒤로가다 내 위치로 돌아온 경우
        # 그럼 카운트를 0으로 바꾸고 끝내버리기
        if last_charge == current:
            charge_count = 0
            break

        #1. 현위치에 충전소가 있을 경우
        if stations[current]:
            # 마지막 충전위치 갱신
            last_charge = current
            # 충전을 했으니, 충전횟수 늘리기
            charge_count += 1
            # 다시 최대 전진
            current += K
        #2. 현위치에 충전기가 없는 경우
        else :
            current -= 1

    print('#{} {}'.format(tc, charge_count))