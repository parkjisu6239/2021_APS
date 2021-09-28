# 참고 : https://vixxcode.tistory.com/23

# N*M 행렬의 각 element의 갯수는 N*M개
# 이때 각 칸을 1 또는 0으로 지정하는 경우의 수 2^(N*M)
# 1을 가로, 0을 세로 (바꿔도 상관없음) 방향으로 잘랐다고 생각하면 문제의 요구사항이 된다.
# 이차원 배열을 각 칸에 비트마스킹으로 인덱싱을 하여 문제를 풀 수 있다.

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(R)]

answer = 0

for i in range(1 << R*C):
    total = 0
    for r in range(R):
        row_sum = 0
        for c in range(C):
            idx = r * C + c
            if i & (1 << idx):
                row_sum = row_sum * 10 + arr[r][c]
            else:
                total += row_sum
                row_sum = 0
        total += row_sum

    for c in range(C):
        col_sum = 0
        for r in range(R):
            idx = r * C + c
            if not (i & (1 << idx)):
                col_sum = col_sum * 10 + arr[r][c]
            else:
                total += col_sum
                col_sum = 0
        total += col_sum

    answer = max(total, answer)

print(answer)
