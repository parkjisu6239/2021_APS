def solution(people, limit):
    people.sort()
    # 보트수, 시작끝인덱스
    cnt = 0
    start = 0 # 한턴에 가능한한 많이 +1
    end = len(people) - 1 # 한턴에 한번만 -1
    while start <= end:
        # 제일 무거운 사람 태우고
        boat = people[end]
        while True:
            # 제한 넘지 않는 동안 태울 수 있으면 태우고, 못태우고 그만
            if people[start] + boat <= limit:
                boat += people[start]
                start += 1
            else:
                break
        end -= 1
        cnt += 1

    return cnt

print(solution([70, 80, 50], 100))