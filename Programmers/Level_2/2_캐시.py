def solution(cacheSize, cities):
    # LRU(Least Recently Used) : 가장 최근에 사용된 것들만 캐시에 담는다.
    # 큐를 사용하여 구현 가능하다.
    # 대소구분이 없다 > 모두 대문자로 or 모두 소문자로
    answer = 0
    que = []

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        if city.lower() in que:
            answer += 1
            que.remove(city.lower())
            que.append(city.lower())
        else:
            answer += 5
            if len(que) == cacheSize:
                que.pop(0)
            que.append(city.lower())

    return answer


print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))