import sys
import time
sys.stdin = open('eval_input.txt')
start = time.time()

N, K = map(int, input().split())
items = list(map(int, input().split()))

C = [0] * (K+1)
for i in range(2, len(items)):
    C[items[i]] += 1

multitab = [0] * (K+1)
for n in range(N):
    multitab[items[n]] = 1

cnt = 0
for i in range(2, K):
    C[items[i]] -= 1
    # 이미 멀티탭에 꽂혀 있으면
    if multitab[items[i]]:
        continue

    # 새로 꽂아야 하는 경우
    for m in range(len(multitab)):
        if multitab[m]:
            if C[m] == 0:
                break
            if items[m] not in items[i+1: min(i+N, K)]:
                break
    else:
        m = 0

    cnt += 1
    multitab[m] = 0
    multitab[items[i]] = 1


print(cnt)


print(time.time()-start)