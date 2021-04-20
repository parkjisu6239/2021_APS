import sys
sys.stdin = open('input.txt')

def merge(L, R):
    global cnt # 문제에서 구하라는 경우의 수

    merge_LR = [] # 정렬된 리스트 담을 변수

    l, r = 0, 0 # 인덱스

    while l < len(L) and r < len(R): # 둘다 남아있을 때
        if L[l] <= R[r]: # 작은 거 담고,
            merge_LR.append(L[l])
            l += 1 # 작은쪽 인덱스 +1
        else:
            merge_LR.append(R[r])
            r += 1

    # 둘중하나는 모두 정렬되어서, while문을 나오게 된다
    if l < len(L): # 왼쪽에 미정렬 원소가 남아있으면
        cnt += 1 # 경우의 수
        merge_LR += L[l:] # 남은거 마저 다 넣기
    elif r < len(R):
        merge_LR += R[r:]

    return merge_LR



def merge_sort(arr):
    if len(arr) == 1: # 한개뿐이면 그것만
        return arr

    N = len(arr) # 아니라면
    L = merge_sort(arr[:N // 2]) # 왼쪽 반띵
    R = merge_sort(arr[N // 2:]) # 오른쪽 반띵

    return merge(L, R) # 반반 구해지면 정렬


for tc in range(1, int(input())+1):
    N = int(input())
    number = list(map(int, input().split()))
    cnt = 0
    sorted_num = merge_sort(number)
    print('#{} {} {}'.format(tc, sorted_num[N // 2], cnt))
