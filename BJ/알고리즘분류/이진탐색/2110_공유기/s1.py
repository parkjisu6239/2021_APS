import sys
sys.stdin = open('input.txt')

# input
N, M = map(int, input().split())
homes = [int(input()) for _ in range(N)]

homes.sort()

# 여기서 left, right는 공유기사이 거리의 최소~최대 구간이다.
left = 1 # 공유기 사이 최소 거리
right = homes[-1] - homes[0] # 공유기 사이 최대 거리
result = 0 # 최종 결과 반환


def PutWifi(left, right):
    global result

    while left <= right: # 이진탐색 베이스 케이스와 동일
        mid = (left + right) // 2 # 공유기 사이의 최소 거리
        start = homes[0]
        wifi = 1 # 맨앞엔 무조건 놓을 수 있으니까 1로 시작

        for i in range(1, N): # 두집 사이의 거리 확인
            d = homes[i] - start
            if mid <= d: # 집사이 거리가 지금 확인하려는 거리보다 크면
                wifi += 1 # 그 집에 놓기
                start = homes[i] # 다음집보러 넘기기
            # 아니라면, 첫~둘 -> 첫~셋 -> 첫~넷 식으로 뒷집만 늘리기


        if wifi >= M: # 설치된게 더 많으면 간격을 늘려서 공유기 수를 줄이자
            result = mid
            left = mid + 1
        else: # 설치된게 더 적으면, 간격을 좁혀서 공유기수를 늘리자
            right = mid - 1


PutWifi(left, right)

print(result)


