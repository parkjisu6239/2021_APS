def solution(people, limit):
    # 정렬을 해서 작은값들부터 더해서 해야하나?
    # 정렬 안하고서는 그냥 일단 한명 태우고, 더태울수 있는 사람 조사해서 더 태우기? 없으면 혼자보내기
    # 탐욕법이라면 후자가 맞을듯하다
    answer = 0
    i = 0
    boat = []
    boat.append(people.pop(0))
    while people:
        if i >= len(people):
            answer += 1
            boat = []
            boat.append(people.pop(0))
            i = 0
            if not people:
                answer += 1
                boat = []
                break
        elif sum(boat) + people[i] <= limit:
            boat.append(people.pop(i))
        else:
            i += 1

    if boat: # solution([20,20,20,20,20], 100)
        return answer+1
    return answer

#print(solution([40,80,60,40,49,57,45,96], 100))


def solution2(people, limit):
    # 보트에 이미 타있는 사람의 몸무게와의 합이 LIMIT를 안넘는 사람중 최대값을 태워야함
    answer = 0
    boat = []
    boat.append(people.pop(0))
    while people:
        if sum(boat) + min(people) > limit: # 더 이상 태울 수 없음
            answer += 1
            boat = [] # 보트에 있던 사람은 구하고, 보트를 비워
            boat.append(people.pop(0)) # 무인도 사람중을 한명 태워
            if not people:  # 무인도에 사람이 없으면
                answer += 1 # 횟수를 올리고
                boat = [] # 구출하고, 보트를 비우고
                break # 반복탈출

        # 무인도에 사람이 남아있고, 보트에 더 태울수 있는 경우
        max_idx = 0
        max_weight = 0
        # 태울 수 있는 가장 무거운 사람을 찾아, 리미트 꽉 채워서
        for j in range(len(people)):
            if sum(boat) + people[j] <= limit:
                if people[j] > max_weight:
                    max_idx = j
                    max_weight = people[j]
        # 그 사람을 찾았으면, 태워
        if max_weight:
            boat.append(people.pop(max_idx))


    if boat: # solution([20,20,20,20,20], 100)
        return answer+1
    return answer


print(solution2([20,20,20,20,20,20,30,50,80], 100))