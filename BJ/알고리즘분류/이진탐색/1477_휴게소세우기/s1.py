import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, L = map(int, input().split())
rest = [0] + list(map(int, input().split())) + [L]
rest.sort()
dist = []

for i in range(1, N+2):
    dist.append(rest[i] - rest[i-1])


dist.sort()

def binary_search(l, r):
    if r <= l:
        return l

    m = (l + r) // 2
    value = 0

    for d in dist:
        if d > m:
            cnt, na = divmod(d, m)
            value += cnt
            if na == 0:
                value -= 1

        if value > M:
            return binary_search(m+1, r)

    return binary_search(l, m)



print(binary_search(1, dist[-1]))

