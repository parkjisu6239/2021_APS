import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

n, r = map(int, input().split())


def nCr(n, r):
    parent = 1
    child = 1
    for k in range(1, r+1):
        parent *= n-k+1
        child *= k

    return int((parent/child) % 1000000007)


print(nCr(n, r))