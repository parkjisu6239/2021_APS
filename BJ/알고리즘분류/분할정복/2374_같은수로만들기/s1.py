# 최솟값을 찾는다.
# 아래 반복
# 최대값을 찾는다
# 인접한 원소를 본다
# 한칸 내린다
# 리스트의 모든 원소가 최솟값이 되면 종료

import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

min_val = min(arr)
cnt = 0

while True:
    target = max(arr)

    if target == min_val:
        break

    i = arr.index(target)

    right, left = 0, 0
    rb, lb = i, i
    for k in range(1, N):
        if i + k >= N:
            break

        if arr[i+k] != arr[i] + 1:
            right = arr[i+k]
            rb = i + k - 1

    for t in range(1, N):
        if i - t < 0:
            break

        if arr[i - t] != arr[i] + 1:
            left = arr[i - t]
            lb = i - t + 1

    goal = right if right > left else left

    for j in range(lb, rb + 1):
        arr[j] = goal

    cnt += target - goal

print(cnt)




