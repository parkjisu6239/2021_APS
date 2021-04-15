import sys
import time
sys.stdin = open('input.txt')
start = time.time()

def powerset_recursion(idx, total):
    if idx == N:
        visit[idx].add(total)
        return

    if total in visit[idx]:
        return

    visit[idx].add(total)
    powerset_recursion(idx + 1, total)
    powerset_recursion(idx + 1, total + score[idx])


for tc in range(1, int(input())+1):
    N = int(input())
    score = list(map(int, input().split()))
    cnt = 0
    visit = {idx: set() for idx in range(N+1)}
    powerset_recursion(0, 0)
    print('#{} {}'.format(tc, len(visit[N])))


print((time.time() - start)*1000) # 0.9996891021728516