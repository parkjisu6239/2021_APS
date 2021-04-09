def solution(jobs):
    # 소요시간이 짧은것부터 먼저 처리해야한다.
    # 완전 이진 트리 인덱스 저장할 필요X
    # 이진 힙에 값으로 [요청시간, 소요시간]을 넣고
    # pop으로 짧은것부터 빼서 연산한다.

    tree = [[0, 0] for _ in range(len(jobs) + 1)]

    # 삽입
    def heappush(tree, value):
        nonlocal element_cnt
        element_cnt += 1

        # 1. 값 추가
        tree[element_cnt] = value

        idx = element_cnt
        while idx > 0 and tree[idx][1] < tree[idx // 2][1]:
            tree[idx], tree[idx // 2] = tree[idx // 2], tree[idx]
            idx //= 2

    # 삭제
    def heappop(tree):
        nonlocal element_cnt

        return_value = tree[1]
        tree[1], tree[element_cnt] = tree[element_cnt], 0
        element_cnt -= 1

        parent = 1
        child = parent * 2
        if child + 1 <= element_cnt:
            if tree[child + 1][1] < tree[child][1]:
                child += 1

        while child <= element_cnt and tree[parent][1] > tree[child][1]:
            tree[parent], tree[child] = tree[child], tree[parent]
            parent = child
            child *= 2

            if child + 1 <= element_cnt:
                if tree[child + 1][1] < tree[child][1]:
                    child += 1

        return return_value

    element_cnt = 0

    jobs.sort()
    for job in jobs:
        heappush(tree, job)

    # print(tree)

    answer = 0 # 처리시간의 총합
    realtime = tree[1][0] # 실제 시간
    for _ in range(len(jobs)):
        request, time = heappop(tree)
        answer += time + (realtime - request)
        realtime += time

    return answer//len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 74)
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 72)