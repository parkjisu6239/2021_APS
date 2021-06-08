import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

s, e = map(int, input().split())

while s > 9 or s < 2 or e > 9 or e < 2:
    print('INPUT ERROR!')
    s, e = map(int, input().split())

def gugudan(s, e):

    for i in range(1, 10):
        if s < e:
            for gugu in range(s, e+1):
                if gugu * i < 10:
                    print('{} * {} =  {}'.format(gugu, i, gugu * i), end="   ")
                else:
                    print('{} * {} = {}'.format(gugu, i, gugu * i), end="   ")
        else:
            for gugu in range(s, e-1, -1):
                if gugu * i < 10:
                    print('{} * {} =  {}'.format(gugu, i, gugu * i), end="   ")
                else:
                    print('{} * {} = {}'.format(gugu, i, gugu * i), end="   ")
        print()

gugudan(s, e)