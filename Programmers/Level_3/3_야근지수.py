# sort ; 효율성 실패
def solution(n, works):
    for _ in range(n):
        works.sort()
        works[-1] -= 1

    answer = 0
    for work in works:
        if work > 0:
            answer += work ** 2

    return answer


# heapq ; 통과
# https://littlefoxdiary.tistory.com/3
# https://docs.python.org/3/library/heapq.html
# 테스트 1 〉	통과 (714.90ms, 10.5MB)
# 테스트 2 〉	통과 (750.32ms, 10.5MB)
import heapq

def solution(n, works):
    
    # 최대값을 찾아야해서 최대힙으로 구성 (우선순위, 값)
    max_heap = []
    for work in works:
        heapq.heappush(max_heap, (-work, work))
    
    # 최대값 빼서 -1 하고 다시 넣기
    for _ in range(n):
        max_item = heapq.heappop(max_heap)[1] - 1
        heapq.heappush(max_heap, (-max_item, max_item))
    
    # 제곱해서 더하기
    answer = 0
    for mh in max_heap:
        if mh[1] > 0:
            answer += mh[1] ** 2

    return answer