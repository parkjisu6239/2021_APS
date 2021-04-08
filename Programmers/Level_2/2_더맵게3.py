import heapq

def solution(scoville, K):
    # 기존 리스트를 힙으로 변환
    heapq.heapify(scoville)
    element_cnt = len(scoville)
    mix = 0

        # 삭제
    def heappop(tree):
        nonlocal element_cnt

        return_value = tree[0]
        tree[0], tree[element_cnt] = tree[element_cnt], -1
        element_cnt -= 1

        parent = 1
        child = parent * 2 + 1
        if child + 1 <= element_cnt:
            if tree[child + 1] < tree[child]:
                child += 1

        while child <= element_cnt and tree[parent] > tree[child]:
            tree[parent], tree[child] = tree[child], tree[parent]
            parent = child
            child *= 2 + 1

            if child + 1 <= element_cnt:
                if tree[child + 1] < tree[child]:
                    child += 1

        return return_value


    # 함수 실행

    mix = 0
    while scoville[1] != -1 and scoville[0] < K:
        mix += 1
        new_scovile = heappop(scoville) + heappop(scoville)*2
        heapq.heappush(scoville, new_scovile)

    if scoville[0] >= K:
        return mix
    else:
        return -1

print(solution([1, 2, 3, 9, 10, 12], 7))