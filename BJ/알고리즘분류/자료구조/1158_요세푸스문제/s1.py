import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

arr = list(range(1, N+1))
k = 0

print('<', end="")

while arr:
    k = (k+K-1) % len(arr)
    if len(arr) == 1:
        print('{}>'.format(arr[k]), end="")
    else:
        print('{}, '.format(arr[k]), end="")
    del arr[k]
