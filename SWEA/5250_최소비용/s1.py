import sys
sys.stdin = open('eval_input.txt')


for tc in range(1, int(input())+1):
    N = int(input())
    land = [list(map(int, input().split())) for _ in range(N)]
    cost = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            elif i == 0: # 첫행인경우
                if land[i][j] > land[i][j-1]: # 높은 경우
                    cost[i][j] += land[i][j] - land[i][j-1]
                cost[i][j] += cost[i][j-1] + 1
            elif j == 0: # 첫열인경우
                if land[i][j] > land[i-1][j]: # 높은 경우
                    cost[i][j] += land[i][j] - land[i-1][j]
                cost[i][j] += cost[i-1][j] + 1
            else:
                a, b = cost[i][j-1], cost[i-1][j]
                if land[i][j] > land[i][j - 1]:
                    a += land[i][j] - land[i][j-1]
                if land[i][j] > land[i-1][j]:
                    b += land[i][j] - land[i-1][j]
                cost[i][j] += min(a, b) + 1


    print('#{} {}'.format(tc, cost[N-1][N-1]))


