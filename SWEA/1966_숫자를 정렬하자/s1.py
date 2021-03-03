import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N):
        for j in range(i + 1, N):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    print('#{}'.format(tc), end=" ")
    print(*numbers)