import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    arr.extend(list(map(int, input().split())))
    arr.sort(reverse=True)
    arr = arr[:N]

print(arr[N-1])
