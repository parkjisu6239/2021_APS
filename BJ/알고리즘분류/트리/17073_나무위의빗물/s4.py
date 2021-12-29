import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, W = map(int, input().split())
leaf = [0] * (N+1)
result = 0

for _ in range(N-1):
    v, w = map(int, input().split())
    leaf[w] += 1
    leaf[v] += 1

for i in range(2, N+1):
    if leaf[i] == 1:
        result += 1

print(W/result)

# 입력으로 간선이 주어질 때 리프노드 구하는 방법
# 그냥 간선이 하나인 것 찾으면 됨!

