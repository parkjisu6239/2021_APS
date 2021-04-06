import sys
sys.stdin = open('input.txt')

def pre_order(node):
    global cnt
    if node:
        cnt += 1
        pre_order(tree[node][0])
        pre_order(tree[node][1])



for tc in range(1, int(input())+1):
    E, subroot = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = [[0, 0, 0] for _ in range(E+2)]

    for i in range(E):
        # 왼쪽 자식
        if tree[temp[2*i]][0] == 0:
            tree[temp[2*i]][0] = temp[2*i + 1]
        # 오른쪽 자식
        else:
            tree[temp[2 * i]][1] = temp[2 * i + 1]
        # 부모
        tree[temp[2 * i + 1]][2] = temp[2 * i]

    cnt = 0
    pre_order(subroot)

    print('#{} {}'.format(tc, cnt))