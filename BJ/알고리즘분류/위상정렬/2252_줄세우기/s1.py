import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
front = [0] * (N+1)
visit = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    front[b] += 1


done = 0
line = []
while done < N:
    for i in range(1, N+1):
        if front[i]:
            continue
        if visit[i]:
            continue
        line.append(i)
        visit[i] = 1
        done += 1
        while arr[i]:
            j = arr[i].pop()
            front[j] -= 1

print(*line)


