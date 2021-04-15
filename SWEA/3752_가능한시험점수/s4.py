import sys
import time
sys.stdin = open('input.txt')
start = time.time()

def solution(score):
    visit = [0] * (sum(score)+1)
    result = [0]
    for i in range(N):
        for j in range(len(result)):
            total = result[j]+score[i]
            if not visit[total]:
                visit[total] = 1
                result.append(total)

    return len(result)

for tc in range(1, int(input())+1):
    N = int(input())
    score = list(map(int, input().split()))
    cnt = solution(score)
    print('#{} {}'.format(tc, cnt))


print((time.time() - start)*1000) # 0.9996891021728516