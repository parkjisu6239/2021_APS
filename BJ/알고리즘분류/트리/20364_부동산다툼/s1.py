import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, Q= map(int, input().split())
owner = [0] * (N+1)

for _ in range(Q):
    duck = int(input())
    v = duck
    block = 0
    while v:
        if owner[v] == 1:
            block = v
        v //= 2
    if block == 0:
        owner[duck] = 1
    print(block)
