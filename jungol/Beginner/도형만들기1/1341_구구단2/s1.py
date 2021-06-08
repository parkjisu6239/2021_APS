import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

s, e = map(int, input().split())

def gugudan(s, e):
    k = 1
    if s > e:
        k = -1

    for gugu in range(s, e+k, k):
        for i in range(1, 10):
            if gugu * i < 10:
                print('{} * {} =  {}'.format(gugu, i, gugu * i), end="   ")
            else:
                print('{} * {} = {}'.format(gugu, i, gugu * i), end="   ")
            if i % 3 == 0:
                print()
        print()

gugudan(s, e)