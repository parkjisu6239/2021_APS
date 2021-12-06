import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')
input = sys.stdin.readline


maxH = {0: []}
minH = {0: []}
visit = [0] * 140001
question_no = {}
idx = 0

N = int(input())
for _ in range(N):
    P, L, G = map(int, input().split())
    if minH.get(G, 0) == 0:
        minH[G] = []
        maxH[G] = []
    heappush(minH[G], (L, P, idx))
    heappush(maxH[G], (-L, -P, idx))
    heappush(minH[0], (L, P, idx))
    heappush(maxH[0], (-L, -P, idx))
    visit[idx] = P
    question_no[P] = idx
    idx += 1

M = int(input())
for _ in range(M):
    cmd = list(map(str, input().split()))
    if cmd[0] == "add":
        heappush(minH[int(cmd[3])], (int(cmd[2]), int(cmd[1]), idx))
        heappush(maxH[int(cmd[3])], (-int(cmd[2]), -int(cmd[1]), idx))
        visit[idx] = int(cmd[1])
        question_no[int(cmd[1])] = idx
        idx += 1
    elif cmd[0] == "recommend":
        if int(cmd[2]) == 1:
            while visit[maxH[int(cmd[1])][0][2]] == 0:
                heappop(maxH[int(cmd[1])])

            if visit[maxH[int(cmd[1])][0][2]]:
                print(-maxH[int(cmd[1])][0][1])
        else:
            while visit[minH[int(cmd[1])][0][2]] == 0:
                heappop(minH[int(cmd[1])])

            if visit[minH[int(cmd[1])][0][2]]:
                print(minH[int(cmd[1])][0][1])
    elif cmd[0] == "recommend2":
        if int(cmd[1]) == 1:
            while visit[maxH[0][0][2]] == 0:
                heappop(maxH[0])

            if visit[maxH[0][0][2]]:
                print(-maxH[0][0][1])
        else:
            while visit[minH[0][0][2]] == 0:
                heappop(minH[0])

            if visit[minH[0][0][2]]:
                print(minH[0][0][1])
    elif cmd[0] == "recommend3":
        if int(cmd[1]) == 1:
            while visit[minH[0][0][2]] == 0:
                heappop(minH[0])

            temp = list(minH[0])
            while temp:
                que = heappop(temp)
                if que[0] >= int(cmd[2]):
                    print(que[1])
                    break
        else:
            while visit[maxH[0][0][2]] == 0:
                heappop(maxH[0])

            temp = list(maxH[0])
            while temp:
                que = heappop(temp)
                if -que[0] < int(cmd[2]):
                    print(-que[1])
                    break
    else:
        visit[question_no[int(cmd[1])]] = 0
