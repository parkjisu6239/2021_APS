import sys
from time import time
sys.stdin = open('input.txt')
start = time()

# 힙
from heapq import heappop, heappush

def find_d(x1, y1, x2, y2): # 거리계산
    return (x1-x2)**2 + (y1-y2)**2

# 실행
for tc in range(1, int(input())+1):
    V = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    env = float(input()) # 세율

    visit = [0]*V # 방문체크
    node = 0
    result = 0

    heap = []
    heappush(heap, (0, 0)) # 거리, v번째

    while node < V:
        cur_d, v = heappop(heap) # 힙이 알아서 최소거리로 추출해준다

        if visit[v]:
            continue
        visit[v] = 1

        node += 1
        result += cur_d

        x1, y1 = x[v], y[v] # 좌표
        for w in range(V):
            if v != w and visit[w] == 0: # 서로 다른 정점이고, 방문X
                x2, y2 = x[w], y[w]
                d = find_d(x1, y1, x2, y2) # 거리 계산해서
                heappush(heap, (d, w)) # 힙에 추가


    print('#{} {}'.format(tc, round(result*env), -1))


print(time() - start)