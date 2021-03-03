import sys
sys.stdin = open("input.txt")

# 평균값구하기
N = int(input())
for n in range(1, N+1):
    numbers = list(map(int, input().split()))
    hap = 0
    cnt = 0
    for number in numbers:
        hap += number
        cnt += 1
    print('#{} {}'.format(n, round(hap/cnt)))