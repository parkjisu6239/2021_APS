import sys
sys.stdin = open("eval_input.txt", "r")

def Bus(K, N, M, bus_stop):
    # 현재 버스의 위치, 마지막 충전위치, 충전횟수 초기화
    location = K
    last_charge = 0
    carge = 0
    # 현위치가 종점 전일때 반복
    while location < N:
        # 만약 마지막 충전위치가 내 현위치면 아래 if-else에서 계속 뒤로 가게 된 상황임
        # 그럼 충전소간 거리가 너무 멀어서, 종점 도착이 불가능 하다는 것이므로 0을 리턴함
        if last_charge == location:
            return 0
        # 내 위치가 충전소면, 충전하고, 마지막 충전위치를 현 위치로 지정하고,
        # 풀충 했으니까 난 내가 갈수 있는 만큼 앞으로 감
        if bus_stop[location]:
            carge += 1
            last_charge = location
            location += K
        # 내 위치가 충전소가 아니면, 뒤로 한칸 가기
        else:
            location -= 1
    return carge

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # 정류장의 수만큼 정류장 리스트를 만듬
    bus_stop = [0] * (N+1)
    # 충전소가 있는 정류장의 인덱스를 1로 만듬
    for i in list(map(int, input().split())):
        bus_stop[i] = 1
    print('#{} {}'.format(tc, Bus(K, N, M, bus_stop)))