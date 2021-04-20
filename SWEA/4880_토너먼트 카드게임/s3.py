import sys
sys.stdin = open('input.txt')

def winner(a,b):
    if b == 0 or a[1] == b[1]:
        return a
    if a[1] == 1 :
        if b[1] == 2: return b
        else: return a
    elif a[1] == 2 :
        if b[1] == 3: return b
        else: return a
    elif a[1] == 3 :
        if b[1] == 1: return b
        else: return a

def post_order(node):
    if node:
        if node * 2 + 1 < M:
            a = post_order(node * 2)
            b = post_order(node * 2 + 1)
            card[node] = winner(a, b)
            return card[node]
        else:
            return card[node]


for tc in range(1, int(input())+1):
    N = int(input())
    temp = list(map(int, input().split()))
    if N % 2:
        card = [0]*(N+1)
    else:
        card = [0] * N
    for i in range(len(temp)):
        card.append([i+1, temp[i]])
    M = len(card)
    post_order(1)
    print('#{} {}'.format(tc, card[1][0]))

