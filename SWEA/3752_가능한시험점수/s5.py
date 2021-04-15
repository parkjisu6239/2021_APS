import sys
import time
sys.stdin = open('input.txt')
start = time.time()

def powerset_recursion(idx, total):
    if idx == N:
        visit[idx][total] = 1
        return

    if visit[idx][total]:
        return


    visit[idx][total] = 1
    powerset_recursion(idx + 1, total)
    powerset_recursion(idx + 1, total + score[idx])



for tc in range(1, int(input())+1):
    N = int(input())
    score = list(map(int, input().split()))
    visit = {idx : [0] * (sum(score)+1) for idx in range(N+1)}
    powerset_recursion(0, 0)
    print('#{} {}'.format(tc, sum(visit[N])))


print((time.time() - start)*1000) # 0.9996891021728516