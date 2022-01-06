import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def post_order(preo, ino):
    if len(preo) == 0:
        return
    elif len(preo) == 1:
        print(preo[0], end=' ')
        return
    elif len(preo) == 2:
        print(preo[1], preo[0], end=' ')
        return

    root_idx = ino.index(preo[0])

    in_left = ino[:root_idx]
    in_right = ino[root_idx+1:]

    pre_left = preo[1: len(in_left) + 1]
    pre_right = preo[len(in_left) + 1:]

    post_order(pre_left, in_left)
    post_order(pre_right, in_right)
    print(preo[0], end=" ")


T = int(input())
for _ in range(T):
    N = int(input())
    pre_order = list(map(int, input().split()))
    in_order = list(map(int, input().split()))
    post_order(pre_order, in_order)
    print()

