import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, r, c = map(int, input().split())

quard = {(0, 0): 1, (0, 1): 2, (1, 0) : 3, (1, 1): 4}


def solution(pre, n, r, c):
    if n == c == 0:
        return pre

    i, j = 0, 0
    if r < 2**(n-1):
        i = 0
    else:
        i = 1

    if c < 2 ** (n - 1):
        j = 0
    else:
        j = 1

    place = quard[(i, j)]
    cnt = (place - 1) * 2**(2*n-2)

    r = r % (2**(n-1))
    c = c % (2**(n-1))

    return solution(pre + cnt, n-1, r, c)


print(solution(0, N, r, c))