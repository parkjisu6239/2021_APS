# nCr = nCr-1 + n-1Cr

import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

n, r = map(int, input().split())


def pascal(n, r):
    if n == r or r == 0 or n == 0:
        return 1

    if r == 1:
        return n

    return pascal(n-1, r-1) + pascal(n-1, r)


print(pascal(n, r))
