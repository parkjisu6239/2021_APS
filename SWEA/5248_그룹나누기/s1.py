import sys
sys.stdin = open('input.txt')


def team(start): # BFS
    global team_cnt

    Q = [start]
    visit[start] = 1
    team_cnt += 1

    while Q:
        v = Q.pop(0)
        for w in graph[v]:
            if visit[w] == 0:
                visit[w] = 1
                Q.append(w)


## 실행 ##
for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    temp = list(map(int, input().split()))
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        graph[temp[2*i]].append(temp[2*i+1])
        graph[temp[2*i+1]].append(temp[2*i])


    # 팀짤때 이미 팀에 속한 사람은 더 이상 뽑지 않기 때문에, 방문체크는 글로벌
    visit = [0] * (V+1)
    team_cnt = 0 # BFS 한 횟수

    for i in range(1, V+1):
        if visit[i] == 0: # 아직 팀에 속하지 않은 경우, 함수 실행
            team(i)


    print('#{} {}'.format(tc, team_cnt))


