import sys
sys.stdin = open('input.txt')

def solution(idx, total):
    global min_val
    if idx == N:
        if total < min_val:
            min_val = total
        return

    if total > min_val:
        return

    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            sel[idx] = number[i]
            solution(idx+1, total+number[idx][i])

            visit[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    number = [ list(map(int, input().split())) for _ in range(N)]
    sel = [0] * N # 선택 값
    visit = [0] * N # 방문 열
    min_val = 10 * N
    solution(0, 0)
    # 결과출력
    print('#{} {}'.format(tc, min_val))
