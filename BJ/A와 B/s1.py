import sys
sys.stdin = open('input.txt')

def change(S, T):
    global flag
    if flag:
        return

    if S == T :
        flag = 1
        return

    if len(S) >= len(T) :
        return

    change(S + 'A', T)
    change(S[::-1] + 'B', T)


for tc in range(1, int(input())+1):
    S = input()
    T = input()

    flag = 0
    change(S, T)

    print(flag)


