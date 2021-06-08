import sys
import time
sys.stdin = open('eval_input.txt')
start = time.time()

for tc in range(1, int(input())+1):
    N = int(input())
    work = []
    for _ in range(N):
        work.append(list(map(int, input().split())))

    # 종료시간 빠른 순 정렬
    work.sort(key = lambda x : (x[1]))

    now_working = work[0]
    cnt = 1
    for i in range(1, len(work)):
        if work[i][0] < now_working[1]:
            continue
        else:
            now_working = work[i]
            cnt += 1

    print('#{} {}'.format(tc, cnt))


print((time.time() - start)*1000) # 0.9996891021728516