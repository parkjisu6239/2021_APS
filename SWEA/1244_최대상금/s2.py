## 1244 최대상금
import sys

sys.stdin = open('input.txt', 'r')
import time

start = time.time()



def get_max():
    global max_val, M, count, prices

    if count == 0:  # 다 교환했으면 끝
        if int(''.join(M)) > max_val:  # 구한거랑 비교
            max_val = int(''.join(M))
        return

    for i in range(len(M)):  # 해당 순번부터
        for j in range(i + 1, len(M)):  # 그 뒤에꺼들 교환. 앞에 건 고려할 필요 없지 어처피 앞부터 진행하는거니까
            M[i], M[j] = M[j], M[i]
            count -= 1
            if int(''.join(M)) not in prices[count]:  # 상금리스트에 갈래를 뻗은적이 있는지 없는지. 한번 갔으면 또 안가도 되니까
                prices[count].append(int(''.join(M)))
                get_max()
            M[i], M[j] = M[j], M[i]
            count += 1



testcase = int(input())
for tc in range(1, testcase + 1):
    M, count = map(int, input().split())
    M = list(str(M))
    max_val = 0
    prices = [[] for _ in range(count + 1)]
    if len(M) - 1 < count:
        while len(M) - 1 < count:
            count -= 2
    get_max()
    print('#{} {}'.format(tc, max_val))

##########################################

print()
print("time :", time.time() - start)