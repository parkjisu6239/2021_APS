import sys
sys.stdin = open('eval_input.txt')

def Perm(idx, total):
    global change, min_change
    # total은 모든 색깔의 칠한 줄 수
    # 색칠된 줄 수가 N을 넘거나, 변경 횟수가 이미 최소를 넘어버리면
    if total > N : return
    if change > min_change: return

    if idx == 3:
        if total == N:
            if change < min_change:
                min_change = change
        return

    # 특정 색깔을 몇줄 칠한 것인지(1줄이상~ N-2까지)
    for i in range(1, N - 1):
        sel[idx] = i
        temp_change = 0
        if idx == 0:
            for j in range(i):
                temp_change += M - color[i][0]
        elif idx == 1:
            for j in range(sel[0], sel[0]+i):
                temp_change += M - color[i][1]
        else:
            for j in range(sel[1], sel[1]+i):
                temp_change += M - color[i][2]
        change += temp_change

        Perm(idx + 1, total + i)
        sel[idx] = 0
        change -= temp_change



for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    flag = [ list(input()) for _ in range(N)]

    # 각 행마다 무슨색이 몇개있는지 부터 확인해보자
    color = []
    for i in range(N):
        # W, B, R
        temp = [0, 0, 0]
        for j in range(M):
            if flag[i][j] == 'W': temp[0] += 1
            elif flag[i][j] == 'B': temp[1] += 1
            else: temp[2] += 1
        color.append(temp)

    # W, B, R를 각각 몇줄 만들지 결정
    sel = [0] * 3
    min_change = 9999999999
    change = 0

    # 인덱스, 중간 합
    Perm(0, 0)

    print(min_change)


