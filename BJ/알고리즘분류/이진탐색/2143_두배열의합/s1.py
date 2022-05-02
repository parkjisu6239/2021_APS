import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))


cumulative1 = {}
for i in range(n):
    for j in range(i, n):
        value = sum(arr1[i:j+1])
        cumulative1[value] = cumulative1.get(value, 0) + 1

cumulative2 = {}
for i in range(m):
    for j in range(i, m):
        value = sum(arr2[i:j + 1])
        cumulative2[value] = cumulative2.get(value, 0) + 1

ans = 0

for key, val in cumulative1.items():
    ans += cumulative2.get(T - key, 0) * val

print(ans)