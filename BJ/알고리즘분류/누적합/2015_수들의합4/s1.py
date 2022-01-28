import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
dic = defaultdict(int)
for i in range(1, N):
    arr[i] += arr[i - 1]

for i in range(N):
    if arr[i] == K:
        cnt += 1
    cnt += dic[arr[i] - K]
    dic[arr[i]] += 1
print(cnt)