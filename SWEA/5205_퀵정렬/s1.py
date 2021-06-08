import sys
sys.stdin = open('eval_input.txt', 'r')

# 파이썬 가변 리스트
def Quick_Sort(arr):
    if len(arr) <= 1:
        return arr

    L, R, pivot = [], [], 0

    for i in range(1, len(arr)):
        if arr[i] <= arr[pivot]: # 작으면 왼쪽
            L.append(arr[i])
        else: # 크면 오른쪽
            R.append(arr[i])

    return Quick_Sort(L) + [arr[pivot]] + Quick_Sort(R) # 정렬한 것 합치기


for tc in range(1, int(input())+1):
    N = int(input())
    number = list(map(int, input().split()))
    sorted_num = Quick_Sort(number)
    print('#{} {}'.format(tc, sorted_num[N // 2]))
