# coding=utf-8
# boj 9334 완전 이진 트리
# 중위 순회

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
no = 1
arr = [0] + list(map(int, input().split()))
result = [0] * len(arr)

def in_order(node):
    global no
    if node > len(arr) - 1:
        return

    in_order(node * 2)
    result[node] = arr[no]
    no += 1
    in_order(node * 2 + 1)

in_order(1)

for i in range(N):
    print(*result[2**i: 2**(i+1)])
