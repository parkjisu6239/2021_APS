import sys
sys.stdin = open("input.txt", "r")

def powersetsum(N, M):
    # 문제에서 1~12 숫자를 원소로 가진 집합이라고 명시됨
    nums = list(range(1,13))
    # 리스트의 크기
    len_nums = len(nums)
    # 부분집합의 갯수를 더해 갈 변수
    cnt = 0
    # nums의 부분 집합 개수 만큼 반복 (2의 n제곱)
    # 원소의 갯수가 처음으로 N개인 부분집합이 처음으로 등장하는 인덱스 : 1 << N -1
    # 1 << N 는 N이 3이라고 하면, 이진수표현으로 1000 (즉, 맨앞 1에,N만큼뒤에 0인 형태)
    # 따라서, 1 << N -1은 N이 3이라고 하면, 이진수표현으로 111 (즉, N만큼 1이 반복)
    # 111 은 처음으로 부분집합의 원소가 3개 등장한 시점임!
    # 그래서 1 << N -1 부터 시작하면 원소가 N개 미만인 반복을 수행하지 않아서 좀 더 빠름
    # (주어진 테케는 작아서 0.02초 밖에 차이 안나긴 함,,)
    # 물론 1 << N -1 다음부터 한다고 해도, 모든 원소의 갯수가 3이상인 것은 아님!
    for i in range(1 << N -1, 1 << len_nums):
        # 부분집합의합과 부분집합원소의 갯수가 N,M과 같을 경우만 최종 결과 cnt에 넣을거라서
        # 각각을 확인하기 위한 변수를 지정
        powerset_sum = 0
        powerset_cnt = 0
        # 리스트의 원소 개수만큼 반복
        for j in range(len_nums):
            if i & (1 << j):
                # 부분집합의 합에 원소를 넣어줌
                powerset_sum += nums[j]
                # 원소의 갯수도 더해줌
                powerset_cnt += 1
                # 그런데 갯수가 N보다 크거나, 합이 M보다 크면 이미 원하는 조건에 부합하지 않으므로
                # 이후 반복을 수행할 필요가 없음!! 그래서 바로 braek하여 불필요한 계산을 줄임!
                if powerset_cnt > N or powerset_sum > M:
                    break
        # 모든 원소를 담았더니, 조건에 부합하면 그때 최종 카운트를 올려줌
        if powerset_cnt == N and powerset_sum == M:
            cnt += 1

    return cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, powersetsum(N, M)))