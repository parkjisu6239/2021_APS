import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

land = [[0] * 101 for _ in range(101)]
result = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            if land[x][y]:
                continue
            land[x][y] += 1
            result += 1

print(result)