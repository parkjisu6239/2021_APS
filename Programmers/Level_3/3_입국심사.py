def solution(n, times):
    max_time = min(times) * n # 소요되는 최대시간(가장 짧은 심사대에서 모두가 다 받는 경우)
    min_time = 1 # 소요되는 최소 시간(1명, 1분)

    while min_time <= max_time: # 역전되는 경우 끝
        mid_time = (min_time + max_time) // 2 # 중간시간
        person = 0 # 심사받은 사람 수

        for time in times:
            person += mid_time // time # 그 시간동안 그 심사대에서 심사받은 사람 수

        if person < n: # 심사를 다 못받음 = 시간을 늘려야함
            min_time = mid_time + 1
        else: # 심사를 다 받고, 혹은 넘침 = 시간을 줄여야함
            max_time = mid_time - 1
            result = mid_time # 그때의 시간도 result에 담기

    return result

# result 매번 갱신하는 이유
# 예제에서 28도, 29도 둘다 위 방법으로는 정답이지만
# 더 작은 28이 나올때 최종적으로 종료해야 한다.
# 그래서 값이 딱 n일때가 아니라, 교차될때까지 계속 돌리고, while이 종료되면 그때의 result를 출력

print(solution(6, [7, 10]))