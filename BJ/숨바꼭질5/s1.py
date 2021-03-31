N = 17
K = 5

que = [(N, 0)]

def BFS(que, K):
    while que:
        position = que.pop(0)

        if position[0] == K:
            return position[1]

        K += position[1]+1

        que.append((position[0]+1, position[1]+1))
        que.append((position[0]*2, position[1] + 1))
        que.append((position[0] -1, position[1] + 1))

BFS(que, K)