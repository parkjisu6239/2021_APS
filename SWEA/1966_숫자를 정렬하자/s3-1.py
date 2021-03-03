"""
3-1. 퀵 정렬 - 고정 배열

- 튜터 -> 디버거 활용하기
- 학습한 내용을 공유하기
"""

import sys
sys.stdin = open('input2.txt')

def partition(arr, start, end):
    # pivot 설정
    pivot = arr[start]
    left = start + 1
    right = end
    done = False

    while not done:
        # 왼쪽(left) -> 오른쪽 이동 조건 (pivot보다 큰 값을 만날 때까지)
        while left <= right and arr[left] <= pivot:
            left += 1
        # 오른쪽(left) -> 왼쪽 이동 조건 (pivot보다 작은 값을 만날 때까지)
        while left <= right and pivot <= arr[right]:
            right -= 1
        # 크로스되면 
        if right < left:
            # 끝
            done = True
        # 교환
        else:
            arr[left], arr[right] = arr[right], arr[left]
    # pivot과 right값 변경 -> pivot을 기준으로 왼/오 정렬 완료
    arr[start], arr[right] = arr[right], arr[start]
    # 자리가 고정된(정렬된) 값(right) return 
    return right

def quick_sort(arr, start, end):
    if start < end:
        # pivot 결정
        pivot = partition(arr, start, end)
        # pivot을 기준으로 왼쪽
        quick_sort(arr, start, pivot-1)
        # pivot을 기준으로 오른쪽을 재귀적으로 호출
        quick_sort(arr, pivot+1, end)
    # 정렬된 리스트 return
    return arr

numbers = list(map(int, input().split()))

print('정렬 전')
print(numbers)

result = quick_sort(numbers, 0, len(numbers)-1)

print('---------------------------------')
print('정렬 후')
print(result)