import sys
sys.stdin = open('input.txt')

def post_order(node):
    # 유효한 경우
    if node <= N and tree[node] == 0:
        a = post_order(node*2)
        b = post_order(node*2+1)
        tree[node] = a+b
        return tree[node]
    # 인덱스 넘어간 경우 없는 자식이니까 0
    elif node > N:
        return 0
    # 인덱스는 안넘어갔는데 거기 이미 값이 있으면, 그거만 리턴
    else:
        return tree[node]

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]
    for _ in range(M):
        idx, val  = map(int, input().split())
        tree[idx] = val

    post_order(1)
    print('#{} {}'.format(tc, tree[L]))