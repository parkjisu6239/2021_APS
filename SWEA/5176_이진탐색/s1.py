import sys
sys.stdin = open('eval_input.txt')

def maketree(node):
    # 숫자가 채워지는 규칙이 중위탐색과 같음
    global cnt

    if node and node <= N:
        maketree(node*2)
        # tree 값이 갱신될때 마다
        tree[node] = cnt
        # cnt += 1
        cnt += 1
        maketree(node * 2 + 1)


for tc in range(1, int(input())+1):
    N = int(input())
    tree = [ 0 for _ in range(N+1)]
    cnt = 1
    maketree(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))

