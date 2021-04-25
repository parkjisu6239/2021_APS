import sys
sys.stdin = open('input.txt')

N, money = map(int, input().split())
coin = [int(input()) for _ in range(N)]
coin = coin[::-1]

cnt = 0
i = 0
while money > 0:
    mok, money = divmod(money, coin[i])
    cnt += mok
    i += 1

print(cnt)