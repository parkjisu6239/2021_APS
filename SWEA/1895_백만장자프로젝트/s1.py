import sys
sys.stdin = open('eval_input.txt')

for tc in range(1 ,int(input())+1):
    N = int(input())
    sise = list(map(int, input().split()))
    # 마지막 시세 처리를 위해 0 추가, 마지막까지 안판게 남았으면 팔게 하기 위해
    sise.append(-100)

    # 오르는 중일때 산다
    # 다음날떨어지면 판다
    money = 0
    cnt = 0
    for i in range(len(sise)-1):
        # 산다.
        if sise[i] <= sise[i+1]:
            money -= sise[i]
            cnt += 1
        # 판다.
        else:
            money += sise[i] * cnt
            cnt = 0

    print('#{} {}'.format(tc, money))
