import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution(w, k):
    loca = defaultdict(list)
    for idx, alpha in enumerate(w):
        loca[alpha].append(idx)

    MIN, MAX = 10000, 0
    for key, val in loca.items():
        if len(val) < k:
            continue

        for i in range(k-1, len(val)):
            length = val[i] - val[i-k+1] + 1
            if length < MIN:
                MIN = length

            if length > MAX:
                MAX = length

    if MAX == 0:
        print(-1)
    else:
        print(MIN, MAX)


t = int(input())
for _ in range(t):
    w = input().rstrip()
    k = int(input())
    solution(w, k)


