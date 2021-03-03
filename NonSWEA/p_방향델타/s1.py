import sys
from pandas import DataFrame as df
sys.stdin = open("input.txt", "r")

N = int(input())
matrix = [ list(map(int, input().split())) for _ in range(N)]
#print(df(matrix))

# 현재 위치 -> (1, 1)
x = 1
y = 1

# 이동 , 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(4):
    # x, y : 기존 위치의 좌표
    # dx[i], dy[i] 변화량
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue
    print(matrix[nx][ny])