import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline

R, C = map(int, input().split())
arr = [ list(input()) for _ in range(R) ]

result = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
que = [(0, 0)]
distance = [[-1] * R for _ in range(C)]
distance[0][0] = 0

while que:
    r, c = que.pop(0)
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < R and 0 <= nc < C and distance[nr][nc] == -1 and arr[nr][nc] not in arr[r][c]:
            arr[nr][nc] += arr[r][c]
            distance[nr][nc] = distance[r][c] + 1
            que.append((nr, nc))

print(arr)

