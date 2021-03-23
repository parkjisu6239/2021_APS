import math

def solution(n, stations, w):
    # n : 아파트 수, stations : 기지국 설치된 아파트, w : 전파 도달 거리
    # 전파가 도달되지 않는 아파트들 중 가장 많은 아파트를 커버하게 끔 기지국을 설치해야 한다
    # 전파 미도달 아파트들의 총 개수 // (2 * w + 1) 만큼 기지국 필요
    # 전파 미도달 구간은 stations 갯수 + 1 만큼
    apartment = list(range(1, n+1))
    answer = 0

    for station in stations:
        apartment.remove(station)
        for i in range(1, w+1):
            if station - i >= 1:
                apartment.remove(station - i)
            if station + i <= n:
                apartment.remove(station + i)

    temp = 1
    for a in range(len(apartment)-1):
        if apartment[a+1] -  apartment[a] == 1:
            temp += 1
        else:
            answer += math.ceil(temp / (2 * w + 1))
            temp = 1

    answer += math.ceil(temp / (2 * w + 1))

    return answer


#print(solution(11, [4, 11], 1))



def solution2(n, stations, w):
    # n : 아파트 수, stations : 기지국 설치된 아파트, w : 전파 도달 거리
    # 전파가 도달되지 않는 아파트들 중 가장 많은 아파트를 커버하게 끔 기지국을 설치해야 한다
    # 전파 미도달 아파트들의 총 개수 // (2 * w + 1) 만큼 기지국 필요
    # 전파 미도달 구간은 stations 갯수 + 1 만큼
    apartment = list(range(1, n+1))

    answer = 0

    for i in range(len(stations)):
        if i == 0:
            if stations[i]-w-1 > 0:
                nosignal1 = apartment[:stations[i]-w-1]
                answer += math.ceil(len(nosignal1) / (2 * w + 1))

            if len(stations) == 1:
                if stations[i] + w < n:
                    nosignal2 = apartment[stations[i] + w:]
                    answer += math.ceil(len(nosignal2) / (2 * w + 1))

        elif i != len(stations) - 1:
            if stations[i] + w < n and stations[i+1] - w - 1 > 0 and stations[i] + w < stations[i+1] - w - 1:
                nosignal = apartment[stations[i] + w  :stations[i+1] - w - 1]
                answer += math.ceil(len(nosignal) / (2 * w + 1))

        else:
            if stations[i - 1] + w < 12 and stations[i] - w - 1 > 0 and stations[i - 1] < stations[i] - w - 1:
                nosignal1 = apartment[stations[i - 1] + w:stations[i] - w - 1]
                answer += math.ceil(len(nosignal1) / (2 * w + 1))

            if stations[i] + w < 12:
                nosignal2 = apartment[stations[i] + w:]
                answer += math.ceil(len(nosignal2) / (2 * w + 1))

    return answer

print(solution2(11, [4, 11], 5))