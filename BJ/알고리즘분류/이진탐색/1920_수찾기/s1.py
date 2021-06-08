import sys
sys.stdin = open('eval_input.txt')

# input
N = int(input())
nums = list(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))


# 정렬
nums.sort()

# 재귀 탐색
def binary_search(target, left, right):
    if left > right:
        return 0

    mid = (left + right) // 2
    if target == nums[mid]:
        return 1
    elif target < nums[mid]:
        return binary_search(target, left, mid-1)
    else:
        return binary_search(target, mid+1, right)


for target in targets:
    print(binary_search(target, 0, N-1))

