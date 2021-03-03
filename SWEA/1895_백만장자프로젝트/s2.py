import sys
sys.stdin = open('input.txt')

for tc in range(1 ,int(input())+1):
    N = int(input())
    sise = list(map(int, input().split()))

    # 뒤에서부터 확인
    idx = len(sise) - 1
    money = 0

    # 맨 앞까지 체크
    while idx > 0:
        # 전날 ~ 첫날 가격 확인
        for i in range(idx-1, -1, -1):
            # 전날 가격이 현시점보다 낮다면, 시세차익을 얻는다.
            if sise[idx] > sise[i]:
                money += sise[idx] - sise[i]
            # 가격이 더 높은 날이 있다면, idx를 그때로 바꾼다.
            else:
                idx = i
                break
        # 현시점 기준 과거의 가격이 모두 낮으면, 검사가 완료되었고
        # 반복문이 break 없이 종료되었으므로, 더 이상 확인할 필요 X
        else:
            break

    print('#{} {}'.format(tc, money))
