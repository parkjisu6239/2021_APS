import sys
from heapq import heappush
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    nums = list(map(int, input().split()))

    heap = []
    for i in nums:
        heappush(heap, i)

    # 인덱스 맞추기 위해
    heap = [0] + heap

    # 연산
    result = 0
    idx = N//2
    while idx > 0:
        result += heap[idx]
        idx //= 2

    print('#{} {}'.format(tc, result))


