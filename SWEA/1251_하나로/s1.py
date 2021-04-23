import sys
from time import time
sys.stdin = open('input.txt')
start = time()


def find_d(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2


for tc in range(1, int(input())+1):
    V = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    env = float(input())


    distance = [987654321987654321] * V
    visit = [0]*V
    visit[0] = 1
    distance[0] = 0
    node = 0

    v = 0
    while node < V-1:
        x1, y1 = x[v], y[v]
        for w in range(V):
            if v != w and visit[w] == 0:
                x2, y2 = x[w], y[w]
                d = find_d(x1, y1, x2, y2)
                if d < distance[w]:
                    distance[w] = d

        min_d = 987654321987654321
        for k in range(len(distance)):
            if visit[k] == 0 and distance[k] < min_d:
                min_d = distance[k]
                v = k

        visit[v] = 1
        node += 1

    print('#{} {}'.format(tc, round(sum(distance)*env), -1))


print(time() - start)