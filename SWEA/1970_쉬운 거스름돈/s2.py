import sys
sys.stdin = open("input.txt", "r")


changes = [ 50000, 10000, 5000, 1000, 500, 100, 50, 10 ]
for tc in range(1, int(input())+1):
    money = int(input())

    print('#{}'.format(tc))
    for i in range(len(changes)):
        # 거스름돈보다 머니가 크면 = money // changes[i] >= 1
        if money // changes[i] >= 1:
            # 몫을 출력
            print((money // changes[i]), end=' ')
            # 돈은 그 화폐로 거슬러주고 남은 돈
            money %= changes[i]
        # 거스름돈이 더 크면
        else:
            # 그 지폐를 못 거슬러준거니까 0
            print(0, end=' ')
    print()