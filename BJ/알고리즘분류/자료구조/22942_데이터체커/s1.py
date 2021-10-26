import sys
sys.stdin = open('input.txt')

N = int(input())
circles = [tuple(map(int, input().split())) for _ in range(N)]


def solution():
    for c1, r1 in circles:
        for c2, r2 in circles:
            if (c1, r1) == (c2, r2):
                continue

            d = abs(c1 - c2)
            if r1 + r2 < d or d < abs(r1 - r2) or d == 0:
                continue
            else:
                return "NO"

    return "YES"


print(solution())