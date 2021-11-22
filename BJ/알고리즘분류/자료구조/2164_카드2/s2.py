import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = deque(range(1, N+1))

while len(arr) > 1:
    arr.popleft()
    arr.append(arr.popleft())

print(arr[0])