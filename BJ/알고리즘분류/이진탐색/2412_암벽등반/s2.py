import sys
from _collections import deque, defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline


N, T = map(int, input().split())
visited = defaultdict(set)
for _ in range(N):
    x, y = tuple(map(int, input().split()))
    visited[x].add(y)
que = deque([[0, 0, 0]])

while que:
    x, y, cnt = que.popleft()
    if y == T:
        print(cnt)
        break
    for xx in range(max(0, x-2), x+3, 1):
        for yy in range(max(0, y-2), y+3, 1):
            if yy in visited[xx]:
                visited[xx].remove(yy)
                que.append([xx, yy, cnt+1])
else:
    print(-1)
