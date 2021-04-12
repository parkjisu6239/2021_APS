import sys
sys.stdin = open('input.txt')

def change(A, B, cnt):
    global result

    if A == B:
        if cnt < result:
            result = cnt
        return

    if A > B:
        return

    change(A * 2, B, cnt+1)
    change(int(str(A) + '1'), B, cnt+1)


for tc in range(1, int(input())+1):
    A, B = map(int,input().split())
    result = 999999

    change(A, B, 0)

    if result == 999999:
        result = -2

    print('#{} {}'.format(tc, result + 1))