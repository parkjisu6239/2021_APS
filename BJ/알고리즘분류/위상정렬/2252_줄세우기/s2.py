import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

# A -> B 순서로 있어야 할 때, B 보다 A가 먼저 있어야 한다.
# front: 그 idx의 학생 보다 먼저 와야할 학생 수.
# arr: 그 idx의 학생 보다 뒤에 올 학생 수.
# que: 지금 줄에 세울 수 있는 학생들.
# 먼저 올 학생 수가 0이면, 지금 줄에 세우면 된다.

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
front = [0] * (N+1)
que = []


for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    front[b] += 1

for i in range(1, N+1):
    if front[i] == 0: # 먼저와야하는 학생 없으면
        que.append(i) # 줄세우기 가능

line = []
while que:
    i = que.pop(0) # 줄세울 수 있는 학생
    line.append(i) # 줄 세우고
    for j in arr[i]: # 위 학생 뒤에 와야 되는 학생들
        front[j] -= 1 # 앞에 서야 되는 i 학생이 줄 섰으니까, 앞에 와야할 학생수 - 1
        if front[j] == 0: # 앞에 올 학생 수가 0이 되면
            que.append(j) # 걔도 줄세우기

print(*line)


