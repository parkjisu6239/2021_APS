import heapq

def solution(scoville, K):
    # 기존 리스트를 힙으로 변환
    heapq.heapify(scoville)
    mix = 0

    # heap은 모든 원소가 항상 정렬된 상태로 유지되는 리스트형 자료구조
    while scoville[0] < K:
        # 0번째 원소가 K 보다 작고, 그거 하나 뿐이면 -1
        if len(scoville) == 1:
            return -1

        # 아니면 순한맛 + 덜 순한맛*2 해서 넣기
        spicy_0 = heapq.heappop(scoville)
        spicy_1 = heapq.heappop(scoville)
        heapq.heappush(scoville, spicy_0 + spicy_1*2)
        mix += 1

    return mix


print(solution([1, 2, 3, 9, 10, 12], 7))
