import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = [float(input().rstrip()) for _ in range(N)]
ans = []

for i in range(N):
    temp = []
    val = arr[i]
    temp.append(val)
    for j in range(i+1, N):
        val *= arr[j]
        temp.append(val)
    ans.append(max(temp))

print(round(max(ans), 3))
