from heapq import heappush, heappop
def solution(jobs):
    heap = []
    for request, time in jobs:
        heappush(heap, (request+time, request, time))

    print(heap)
    now_time = heap[0][1]
    result = 0
    while heap:
        end, start, time = heappop(heap)
        if now_time > start:
            result += (now_time-start) + time
            now_time += time
        else:
            now_time = end
            result += time


    return result // len(jobs)



print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 74)
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 72)