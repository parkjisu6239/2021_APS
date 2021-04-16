import sys
import time
sys.stdin = open('input.txt')
start = time.time()

N, K = map(int, input().split())
items = list(input().split())

def solution(idx, multitab, cnt):
    global result
    if idx == K:
        if cnt < result:
            result = cnt
        return

    if cnt > result:
        return

    if visit.get((idx, ''.join(multitab), cnt), 0):
        return

    visit[(idx, ''.join(multitab), cnt)] = 1

    if items[idx] not in multitab:
        for i in range(len(multitab)):
            old = multitab[i]
            multitab[i] = items[idx]

            solution(idx+1, multitab, cnt+1)

            multitab[i] = old
    else:
        solution(idx + 1, multitab, cnt)



result = 150
multitab = items[:N]
visit = dict()
solution(2, multitab, 0)
print(result)


print(time.time()-start)
