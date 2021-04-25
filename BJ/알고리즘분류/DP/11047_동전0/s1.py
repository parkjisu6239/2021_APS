import sys
sys.stdin = open('input.txt')

N, money = map(int, input().split())
coin = [int(input()) for _ in range(N)]
coin = coin[::-1]

min_cnt = money*10
start = 0
flag = 1
while start < N and flag:
    copy_money = money
    cnt = 0
    i = start
    while copy_money > 0:
        if cnt > min_cnt:
            flag = 0
            break
        mok, copy_money = divmod(copy_money, coin[i])
        cnt += mok
        i += 1

    min_cnt = min(cnt, min_cnt)
    start += 1


print(min_cnt)