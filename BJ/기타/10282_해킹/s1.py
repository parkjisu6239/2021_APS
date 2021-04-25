import sys
sys.stdin = open('input.txt')

for _ in range(int(input())):

    V, E, hack = map(int, input().split())
    graph = [[9999] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w
        graph[e][s] = w

    visit = [9999] * (V+1)
    visit[hack] = 0
    que = [hack]
    infection = 0

    while que:
        v = que.pop(0)
        for w in range(len(graph[v])):
            if graph[v][w] and graph[v][w] + visit[v] < visit[w]:
                visit[w] = graph[v][w] + visit[v]
                infection += 1
                que.append(w)

    last_time = 0
    for time in visit:
        if time != 9999 and time > last_time:
            last_time = time

    print(infection, last_time)








