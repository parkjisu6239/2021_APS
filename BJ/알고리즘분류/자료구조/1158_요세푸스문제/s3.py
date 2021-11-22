import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

arr = list(range(1, N+1))
k = 0
ans = []

while arr:
    k = (k+K-1) % len(arr)
    ans.append(str(arr.pop(k)))

print("<", ", ".join(ans), ">", sep="")

