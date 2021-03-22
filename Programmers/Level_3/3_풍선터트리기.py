def solution(a):
    # swea 등산로 문제와 유사?
    # 1. 임의의 인접한 두 풍선 선택
    # 2. 작은걸 터친적 있는지 없는지에 따라, 큰 풍선 또는 작은 풍선 터침
    # 3. 위 경우를 풍선이 한개 남을때까지 반복
    # 4. 한개남은 풍선은 결과에 set으로 저장
    answer = set()

    def balloon(balloons, is_pop_small):
        nonlocal answer
        # 한개뿐이라면 결과에 저장
        if len(balloons) == 1:
            answer.add(balloons[0])
            return

        # 2개 이상인 경우 터치기
        for i in range(len(balloons) - 1):
            # 작은걸 터친적 있으면, 무조건 큰걸 터져라
            if is_pop_small:
                if balloons[i] > balloons[i + 1]:
                    balloon(balloons[:i] + balloons[i + 1:], is_pop_small)
                else:
                    balloon(balloons[:i + 1] + balloons[i + 2:], is_pop_small)
            # 작은거 터친적 없으면, 작은거 or 큰거 터칠거골라서 터쳐라
            else:
                if balloons[i] > balloons[i + 1]:
                    # 큰걸 터지는 경우
                    balloon(balloons[:i]+balloons[i+1:], is_pop_small)
                    # 작은걸 터치는 경우, is_pop_small 1
                    balloon(balloons[:i+1] + balloons[i + 2:], 1)
                else:
                    # 큰걸 터지는 경우
                    balloon(balloons[:i+1] + balloons[i + 2:], is_pop_small)
                    # 작은걸 터치는 경우, is_pop_small 1
                    balloon(balloons[:i] + balloons[i + 1:], 1)

    balloon(a, 0)

    return len(answer)


print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))