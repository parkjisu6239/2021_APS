import sys
from pandas import DataFrame as df
sys.stdin = open("input.txt")

N, M = map(int, input().split())
office = [ list(map(int, input().split())) for _ in range(N) ]
print(office)

# CCTV는 회전 가능, 감시는 수직수평만 가능
# 0은 빈칸, 6은 벽, 1~5는 CCTV