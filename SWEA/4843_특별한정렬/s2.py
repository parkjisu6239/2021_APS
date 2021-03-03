import sys
sys.stdin = open('input.txt', 'r', encoding = 'UTF-8')

def special_sort(N, numbers):
    # 선택정렬
    # 나를 최대값(내림차순) or 최솟값(오름차순)이라고 가정하고,
    # 나 다음부터~끝중에 최대값 or 최솟값을 찾아서 나랑 자리 바꾸기
    for i in range(10):
        # 인덱스가 홀수이면(1번째 부터 시작할 경우, 짝수번째 수)
        if i % 2:
            # 나를 최소값이라고 하자
            min_idx = i
            for j in range(i+1, N):
                # 나보다 작으면, 걔를 최솟값이라고 하자
                if numbers[j] < numbers[min_idx]:
                    min_idx = j
            # 찐 최소값을 찾으면, 나랑 걔랑 자리 바꾸자
            numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
        # 인덱스가 짝수이면(1번째 부터 시작할 경우, 홀수번째 수)
        else:
            # 나를 최대값이라고 하자
            max_idx = i
            for j in range(i+1, N):
                # 나보다 크면, 걔를 최대값이라고 하자
                if numbers[j] > numbers[max_idx]:
                    max_idx = j
            # 찐 최대값을 찾으면, 나랑 걔랑 자리 바꾸자
            numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]

    return ' '.join(map(str, numbers[:10]))

for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(tc, special_sort(N, numbers)))