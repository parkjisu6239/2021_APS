import sys
sys.stdin = open('input.txt', 'r', encoding = 'UTF-8')

def special_sort(N, numbers):

    sorted_number = []
    while len(sorted_number) < 10 and len(numbers) > 0:
        min_idx = 0
        max_idx = 0
        # 최대최소를 구해서 각각 sorted_number에 담기
        for i in range(len(numbers)):
            if numbers[i] > numbers[max_idx]:
                max_idx = i
            if numbers[i] < numbers[min_idx]:
                min_idx = i
        sorted_number.append(numbers[max_idx])
        sorted_number.append(numbers[min_idx])

        # remove를 안쓰려고 이렇게 구성했습니다
        if max_idx > min_idx:
            a, b = min_idx, max_idx
        else:
            a, b = max_idx, min_idx
        numbers = numbers[:a] + numbers[a+1:b] + numbers[b+1:]

    return ' '.join(map(str, sorted_number))

for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(tc, special_sort(N, numbers)))