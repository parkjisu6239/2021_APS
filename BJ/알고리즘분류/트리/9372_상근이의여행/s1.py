import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    for __ in range(M):
        a, b = map(int, input().split())
    print(N-1)

