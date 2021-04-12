import sys
sys.stdin = open('input.txt')

def zoo(N, info):
    count = []

    for i in range(N):
        if i in info:
            if (count and info.count(i) > count[-1]) or (info.count(i) > 2):
                return 0
            count.append(info.count(i))

    if count:
        animal1 = len(count)
        animal2 = len(count) - (count[-1] % 2)

    return 0

for tc in range(1, int(input())+1):
    N = int(input())
    info = list(map(int, input().split()))
    print(zoo(N, info))

