import sys
sys.stdin = open("input.txt", "r")

def two_number_list(N, M):
    # 편의상 A가 작은 수, B가 큰수로 세팅
    if N > M:
        N, M = M, N
        B = list(map(int, input().split()))
        A = list(map(int, input().split()))
    else:
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))


    # 최댓값 초기화, 첫번째 구간합 미리 구해두기
    max_sum = 0
    for i in range(N):
        max_sum += A[i] * B[i]

    # 위에서 첫번째 구간합 구했으니, 여기서는 인덱스 1부터 시작
    for i in range(1, M-N+1):
        my_sum = 0
        for j in range(N):
            my_sum += A[j] * B[i+j]
        if max_sum < my_sum:
            max_sum = my_sum
    return max_sum


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, two_number_list(N, M)))