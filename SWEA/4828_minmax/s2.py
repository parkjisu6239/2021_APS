import sys
sys.stdin = open("eval_input.txt", "r")

def minmax(N):
    numbers = list(map(int, input().split()))

    my_min = my_max = numbers[0]
    for i in range(1, N):
        if my_max < numbers[i]:
            my_max = numbers[i]
        if my_min > numbers[i]:
            my_min = numbers[i]

    return my_max - my_min

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{} {}'.format(tc, minmax(N)))
