import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')
input = sys.stdin.readline


maxH = []
minH = []
visit = [0] * 140001
question_no = {}
idx = 0

N = int(input())
for _ in range(N):
    P, L = map(int, input().split())
    heappush(minH, (L, P, idx))
    heappush(maxH, (-L, -P, idx))
    visit[idx] = P
    question_no[P] = idx
    idx += 1

M = int(input())
for _ in range(M):
    cmd = list(map(str, input().split()))
    if cmd[0] == "add":
        heappush(minH, (int(cmd[2]), int(cmd[1]), idx))
        heappush(maxH, (-int(cmd[2]), -int(cmd[1]), idx))
        visit[idx] = int(cmd[1])
        question_no[int(cmd[1])] = idx
        idx += 1
    elif cmd[0] == "recommend":
        if int(cmd[1]) == 1:
            while maxH and visit[maxH[0][2]] == 0:
                heappop(maxH)

            if maxH and visit[maxH[0][2]]:
                print(-maxH[0][1])
        else:
            while minH and visit[minH[0][2]] == 0:
                heappop(minH)

            if minH and visit[minH[0][2]]:
                print(minH[0][1])
    else:
        visit[question_no[int(cmd[1])]] = 0
