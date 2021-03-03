import sys

sys.stdin = open("input.txt", "r")

'''
# 내풀이
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    # 초기값 설정
    # max는 max보다 클때 담아져서, 0으로 해도 반복문 시작부터 담길 수 있음
    # min은 0으로 하면 값이 변경되지 않아서, 첫 구간합으로 지정
    max_value = 0
    min_value = sum(numbers[0:M])

    for i in range(N-M+1):
        if min_value > sum(numbers[i:i+M]):
            min_value = sum(numbers[i:i+M])
        if max_value < sum(numbers[i:i+M]):
            max_value = sum(numbers[i:i+M])

    result =  max_value - min_value

    print('#{} {}'.format(tc, result))
'''

'''
# 라이브 풀이 min max 미사용
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_value = 0
    min_value = 5732516848749

    for i in range(N-M+1):
        tmp = 0

        for j in range(M):
            tmp += numbers[i+j]

        if max_value < tmp:
            max_value = tmp
        if min_value > tmp:
            min_value = tmp

    print('#{} {}'.format(tc, max_value - min_value))
'''

# 라이브 풀이 구간합 중복구간은 활용
# 구간합 구할때 이전 구간과 앞뒤빼고 가운데부분이 같은 것을 활용
# 다음 구간합을 구할때 이전 구간합에서 맨앞 값을 빼고, 새로추가되는 맨뒤 값만 추가
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    tmp = 0
    for i in range(M):
        tmp += numbers[i]

    max_value = tmp
    min_value = tmp

    for i in range(M, N):
        tmp = tmp + numbers[i] - numbers[i - M]

        if max_value < tmp:
            max_value = tmp
        if min_value > tmp:
            min_value = tmp

    print('#{} {}'.format(tc, max_value - min_value))
