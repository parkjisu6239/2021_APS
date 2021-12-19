# 11725 트리의 부모 찾기
# 루트인 1번부터 다음 뎁스로 찾아 내려가기

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N+1)]
result = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

que = [(1, 1)]
while que:
    me, parent = que.pop()
    result[me] = parent
    for child in arr[me]:
        if result[child]:
            continue
        que.append((child, me))

print(*result[2:], sep="\n")