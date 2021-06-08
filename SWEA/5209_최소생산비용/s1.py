import sys
sys.stdin = open('eval_input.txt', 'r')


def solution(idx, total):
    global min_fee
    if idx == N:
        if total < min_fee:
            min_fee = total
        return

    if total > min_fee:
        return

    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            solution(idx+1, total+price[idx][i])
            visit[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    price = [ list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    min_fee = 9999999999
    solution(0, 0)
    print('#{} {}'.format(tc, min_fee))