import sys
sys.stdin = open('input.txt', 'r', encoding = 'UTF-8')

for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    print('#{}'.format(tc),end=" ")
    numbers.sort()
    for i in range(5):
        print(numbers[N-1-i], end=" ")
        print(numbers[i], end=" ")
    print()