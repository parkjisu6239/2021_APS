import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
stack = []
ans = 0

for _ in range(N):
    x, y = map(int, input().split())
    while stack and y < stack[-1]:
        stack.pop()
        ans += 1

    if stack and y == stack[-1]: continue

    stack.append(y)

for s in stack:
    if s:
        ans += 1

print(ans)