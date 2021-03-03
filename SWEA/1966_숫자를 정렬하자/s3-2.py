"""
3-2. 퀵 정렬 - 가변 배열

- 튜터 -> 디버거 활용하기
- 학습한 내용을 공유하기
"""

import sys
sys.stdin = open('input2.txt')

def quick_sort(numbers):
    N = len(numbers)
    if N <= 1:
        return numbers
    else:
        # pivot은 설정하는 방법이 다양하지만 첫 번째 값을 pivot으로 설정한다고 생각하면 이해하기 쉬워요!
        pivot = numbers[0]
        # 왼/오 리스트 준비하고
        left, right = [], []
        # pivot 다음 값부터 비교한다.
        for idx in range(1, N):
            # 만약 pivot보다 크면
            if numbers[idx] > pivot:
                # 오른쪽 리스트로 가!
                right.append(numbers[idx])
            # pivot보다 작으면
            else:
                # 왼쪽 리스트로가!
                left.append(numbers[idx])
        # 재귀적으로 호출하자
        sorted_left = quick_sort(left)
        sorted_right = quick_sort(right)

        # 왼/오 정렬이 끝나면 합친 리스트를 return
        return [*sorted_left, pivot, *sorted_right]

numbers = list(map(int, input().split()))

print('정렬 전')
print(numbers)

result = quick_sort(numbers)

print('---------------------------------')
print('정렬 후')
print(result)