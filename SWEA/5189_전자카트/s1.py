import sys
import time
sys.stdin = open('eval_input.txt')
start = time.time()

def perm(idx, total):
    global min_val
    # 경로가 끝나면(순열의 길이가 끝나면)
    if idx == N:
        # 마지막 0번으로 돌아가는거까지 더하고
        total += arr[sel[idx-1]][sel[idx]]
        # 최소라면 갱신
        if total < min_val:
            min_val = total
        print(sel)
        return

    if total > min_val:
        return

    # 0번은 마지막에만 갈거라서 1번 인덱스부터
    for i in range(1, N):
        if visit[i] == 0:
            visit[i] = 1
            sel[idx] = i
            # 시점-종점으로 가는 배터리 소비량 더하기
            total += arr[sel[idx-1]][sel[idx]]
            perm(idx+1, total)

            # 재귀에서 빠져 나온 경우 원상복구
            visit[i] = 0
            total -= arr[sel[idx - 1]][sel[idx]]


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    # 경로가 선택될 변수, 맨앞맨뒤는 0으로 고정
    sel = [0] * (N+1)
    # 0~N의 방문체크
    visit = [0] * N
    # 0번 인덱스는 시작점이라 방문 체크 미리
    visit[0] = 1
    min_val = 999999
    perm(1, 0)
    print('#{} {}'.format(tc, min_val))


print((time.time() - start)*1000) # 0.9996891021728516