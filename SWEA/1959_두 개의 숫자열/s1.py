import sys
sys.stdin = open("input.txt", "r")

def func1(N, M, A, B):
    # A, B가 겹치는 구간합의 최대를 찾아야 해서 최대값을 초기화함
    max_val = -999999999

    # M과 N 중 큰것에 따라 다르게 구현
    # 작은 쪽을 이동시키면서 겹치는 구간을 구해야하기 때문!
    # M이 큰경우
    if M > N:
        # A,B 중 긴 구간은 이전문제인 구간합과 마찬가지로, range 조정이 필요
        for i in range(M - N + 1):
            # A, B가 겹치는 구간 합
            # 구간합을 구하기 위해 sum_val 세팅
            sum_val = 0
            # 구간합을 구하는 반복문
            for j in range(N):
                # 짧은쪽(여기서는 N이 작아서 A임)의 인덱스는 항상 0~N 순회
                # 긴쪽의 인덱스는 i를 통해 순회하여 1 더해진 상태에서 j를 더함
                sum_val += A[j] * B[i+j]
            # 위 구간의 구간합이 정해졌을때 max_val보다 크면 변경
            if sum_val > max_val:
                max_val = sum_val
        # 최종적으로 모든 겹치는 구간들의 구간합중 가장 큰 값을 리턴함
        return max_val
    # N이 큰 경우
    elif M < N:
        # 위와 인덱스 선택 방법이 반대
        for i in range(N - M + 1):
            # A, B가 겹치는 구간 합
            sum_val = 0
            for j in range(M):
                sum_val += A[i+j] * B[j]

            if sum_val > max_val:
                max_val = sum_val
        return max_val
    # M과 N이 같은 경우 겹치는 경우가 1개뿐이니, 합만 구해서 리턴!
    else:
        sum_val = 0
        for i in range(N):
            sum_val += A[i] * B[i]
        return sum_val


T = int(input())
for tc in range(1, T+1):
    # 1. 입력받기
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print('#{} {}'.format(tc,func1(N, M, A, B)))

