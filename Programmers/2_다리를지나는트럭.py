def solution(bridge_length, weight, truck_weights):
    # 경과 시간, 다리를 지난 트럭, 다리를 건너는 트럭, 다리에 오른 시점부터 경과 시간
    answer = 0
    bridge_end = []
    bridge_ing = []
    bridge_ing_time = []
    # 대기트럭과, 다리위트럭이 있는 경우 반복
    while len(truck_weights) > 0 or len(bridge_ing) > 0:
        # 경과 시간 +1
        answer += 1
        # 대기트럭이 있을 때
        if len(truck_weights) > 0:
            # 다리를 지나는 트럭의 총무게와, 첫번째 대기트럭 무게의 합을 다리가 견딜 수 있으면
            if sum(bridge_ing) + truck_weights[0] <= weight:
                # 대기트럭을 다리를 지나는 트럭에 넣음
                bridge_ing.append(truck_weights.pop(0))
                # 다리를 지나틑 트럭의 경과 시간을 0으로 bridge_ing_time에 담음
                bridge_ing_time.append(0)

        # 다리 위 트럭의 경과 시간을 늘리고, 다리를 다 지난 트럭을 건넌트럭 리스트에 넣을 반복문
        i = 0
        while i < len(bridge_ing):
            # 다리를 지나는 중인 트럭의 경과시간을 올림
            bridge_ing_time[i] += 1
            # 경과시간이(1초에 길이 1만큼 감) 다리 길이보다 크면
            if bridge_ing_time[i] >= bridge_length:
                # 다리를 다 건넌거니까, 건너는중 리스트에서 빼고 다 건넌 리스트에 넣음
                bridge_end.append(bridge_ing.pop(i))
                # 같은 인덱스에 넣어둔 경과시간도 제거함
                bridge_ing_time.pop(i)
                # 건너는중인 트럭이 여러대 일경우 모두 경과시간을 더해주고, 다 지났는지 확인해야 하니까
                # 인덱스 올리지말고 한번 더 해라
                continue
            i += 1

    return answer + 1


print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))