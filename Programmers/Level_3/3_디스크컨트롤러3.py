from heapq import heappush, heappop
def solution(jobs): # 요청시간, 소요시간
    # 1. 일단 먼저 들어온 순서로 처리
    # 2. 특정 작업을 수행하는 동안 들어온 요청들은 taskheap에 추가

    jobs.sort()
    jobs = [job[::-1] for job in jobs] # 소요시간, 요청시간

    taskheap = [] # 대기실
    callstack = [] # 현재 실행중인 작업
    time = jobs[0][1] # 첫번째 작업의 요청시간(현재 시간, 리얼타임)
    result = 0
    idx = 0
    completed = 0

    while completed < len(jobs):
        if callstack:
            # 현재 작업 처리 도중에 들어온 요청은 대기실에 추가
            while idx < len(jobs) and time - callstack[0] <= jobs[idx][1] <= time:
                heappush(taskheap, jobs[idx])
                idx += 1
        if taskheap:
            callstack = heappop(taskheap)
            result += (time - callstack[1]) + callstack[0] # 대기시간 + 소요시간
            time += callstack[0]
            completed += 1
        else:
            callstack = jobs[idx]
            result += (callstack[0])
            time = callstack[1] + callstack[0]
            idx += 1
            completed += 1

    return result // len(jobs)



print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 74)
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 72)