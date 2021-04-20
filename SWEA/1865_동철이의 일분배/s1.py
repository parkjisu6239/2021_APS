import sys, time
sys.stdin = open('input.txt')
start = time.time()


def dongcheol(idx, percent):
    global max_percent

    # 1 이하 숫자라 곱할수록 작아짐
    # 근데 덜 곱했는데도 벌써 max보다 작아진거면 가망 없음
    if percent <= max_percent:
        return

    if idx == N:
        if percent > max_percent:
            max_percent = percent
        return

    if percent in back_track[idx]:
        return

    back_track[idx].append(percent)

    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            dongcheol(idx+1, percent*(P[idx][i])*0.01)
            visit[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    visit = [0]*N
    back_track = [[] for _ in range(N)]
    max_percent = 0
    dongcheol(0, 1)

    print('#{} {:.6f}'.format(tc, max_percent*100))


print((time.time()-start)*1000)