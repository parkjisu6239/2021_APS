import sys
sys.stdin = open('input.txt')

def post_order(node):
    global tree
    # 유효한 노드인 경우
    if node:
        # 왼쪽 자식 값을 a, 오른쪽 자식 값을 b
        a = post_order(tree[node][1])
        b = post_order(tree[node][2])
        # 그리고 본인을 오퍼레이터로 지정
        operator = tree[node][0]

        # 오퍼레이터가 사칙연산인경우, a,b로 사칙연산
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b
        # 오퍼레이터가 숫자인 경우 오퍼레이터를 반환
        # 후위 순회로 왼>오>부모 찾다가 끝에 다다른 경우(자식이없는경우)
        # 자식이 없어서 node가 0으로 재귀에 들어오게 된다.
        # 결국 a:none, b:none, operator:현재정점의 값
        else:
            return operator


for tc in range(1, 11):
    N = int(input())
    # 값, 왼자식, 오른자식
    tree = [[0,0,0] for _ in range(N+1)]
    for _ in range(N):
        info = input().split()
        for i in range(1, len(info)):
            if info[i].isdigit():
                tree[int(info[0])][i-1] = int(info[i])
            else:
                tree[int(info[0])][i-1] = info[i]


    print('#{} {}'.format(tc, int(post_order(1))))
