import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))

    # sum 안쓰고 sum 구하기
    my_sum = 0
    for number in numbers:
        my_sum += number

    # 평균
    my_average = my_sum/10

    # round 안쓰고 반올림/반내림 하기
    if my_average % 1 >= 0.5:
        my_average = my_average // 1 + 1
    else:
        my_average = my_average // 1

    print('#{} {}'.format(tc, int(my_average)))