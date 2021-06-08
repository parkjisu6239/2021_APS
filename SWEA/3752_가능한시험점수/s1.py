import sys
import time
sys.stdin = open('eval_input.txt')
start = time.time()

def powerset_bin(score):
    result = set()
    for i in range(1 << len(score)):
        total = 0
        for j in range(len(score)):
            if i & (1 << j):
                total += score[j]
        result.add(total)
    return result

for tc in range(1, int(input())+1):
    N = int(input())
    score = list(map(int, input().split()))
    print('#{} {}'.format(tc, len(powerset_bin(score))))


print((time.time() - start)*1000) # 0.9996891021728516