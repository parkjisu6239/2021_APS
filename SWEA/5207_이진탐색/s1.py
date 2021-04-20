import sys
sys.stdin = open('input.txt')

# 이진탐색 탐색시작, 탐색끝, 오른쪽연속선택횟수, 왼쪽연속선택횟수
def binary_search(l, r, target, r_sel, l_sel):
    # 연속선택했거나, target을 찾을 수 없으면(l > r)
    if r_sel == 2 or l_sel == 2 or l > r:
        return 0

    mid = (l + r) // 2

    if target == A[mid]: # 연속선택없이 타겟을 찾으면 1
        return 1
    elif target > A[mid]: # 오른쪽 선택한 경우
        return binary_search(mid+1, r, target, r_sel+1, 0)
    else: # 왼쪽 선택한 경우
        return binary_search(l, mid-1, target, 0, l_sel+1)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort() # 정렬한거 주는줄 알았는데, 정렬하라는거네요 ㅠ
    B = list(map(int, input().split()))
    result = 0
    for b in B:
        result += binary_search(0, N-1, b, 0, 0)
    print('#{} {}'.format(tc, result))