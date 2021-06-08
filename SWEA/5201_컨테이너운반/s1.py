import sys
import time
sys.stdin = open('eval_input.txt')
start = time.time()


for tc in range(1, int(input())+1):
    ct_cnt, tr_cnt = map(int, input().split())
    container = list(map(int, input().split()))
    truck_limit = list(map(int, input().split()))

    container.sort(reverse=True)
    truck_limit.sort(reverse=True)

    c = 0
    t = 0
    total = 0
    while c < ct_cnt and t < tr_cnt:
        if container[c] <= truck_limit[t]:
            total += container[c]
            t += 1
        c += 1

    print('#{} {}'.format(tc, total))





print((time.time() - start)*1000) # 0.9996891021728516