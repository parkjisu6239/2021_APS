import sys
from math import log

sys.setrecursionlimit(10**6)

sys.stdin = open('input.txt')
input = sys.stdin.readline

l, w, h = map(int, input().split())
n = int(input())
boxes = [0] * n

for _ in range(n):
    idx, cnt = map(int, input().split())
    boxes[idx] = cnt

flag = 1


def solution(l, w, h):
    global flag

    if not l or not w or not h:
        return 0

    if flag == 0:
        return 0

    k = min(l, w, h)
    t = int(log(k, 2))

    while True:
        if t < 0:
            flag = 0
            return -1

        if t >= len(boxes) or not boxes[t]:
            t -= 1
            continue

        boxes[t] -= 1
        T = 2**t
        return solution(l-T, T, h) + solution(l, w-T, h) + solution(T, T, h-T) + 1



answer = solution(l, w, h)
print(answer if flag else -1)
