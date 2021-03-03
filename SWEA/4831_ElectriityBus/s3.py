import sys
sys.stdin = open("input.txt", "r")

def Bus(K, N, charger):
    # 남은 배터리, 충전소 인덱스, 충전횟수 초기화
    battery = K
    charge_idx = 0
    charge_cnt = 0
    # 앞으로 한칸씩 갈 것임
    for location in range(1, N):
        # 앞으로 한칸가고, 배터리 1줄이고
        battery -= 1
        # 만약 배터리가 0보다 작아지면, 더이상 진행 불가니까 0을 리턴함
        if battery < 0:
            return 0
        # 내 위치가 충전소이면,
        if location == charger[charge_idx]:
            # 내가 여기서 충전했을때 종점 갈수 있으면, 충전하고 끝!
            if location + K >= N:
                charge_cnt += 1
                break
            # 현재 충전소와 다음 충전소까지의 거리가 배터리보다 적으면
            # 현재 충전소에서 충전할 필요 없으니까, 충전소 인덱스만 올림
            # 충전소 인덱스는 내가 현 충전소를 지나갈때(현위치가 충전소일때) 올림
            elif charger[charge_idx + 1] - location <= battery:
                charge_idx += 1
            # 현재 충전소와 다음 충전소 사이를 충전 없이 갈 수 없으면
            # 여기서 충전 해야됨
            # 풀충하고, 충전횟수 올리고, 충전소 인덱스도 올림
            else:
                battery = K
                charge_cnt += 1
                charge_idx += 1

    return charge_cnt


T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # 정류장의 수만큼 정류장 리스트를 만듬
    charger =  list(map(int, input().split()))
    print('#{} {}'.format(tc, Bus(K, N, charger)))