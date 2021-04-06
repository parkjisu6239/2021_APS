import sys
sys.stdin = open('input.txt')

# 전처리
def treeeee(V):
    # 완전 이진 트리라는 가정 하에
    # 인덱스로 부모, 자식 관계를 파악할 수 있다.
    # 그래서 리스트에는 알파벳만 있으면 된다.
    tree = ['']
    for _ in range(V):
        info = input().split()
        # 알파벳 정보만 담기
        tree.append(info[1])
    return tree


# 순회
def in_order(node):
    # 자식으로 계속 내려갈건데 *2 하면 계속 숫자가 커진다
    # 정점 번호가 정점수보다 작을때만 탐색을 진행하게 한다
    if node <= V:
        in_order(node*2)
        print(tree[node], end='')
        in_order(node*2 + 1)


# 함수 실행
for tc in range(1, 11):
    V = int(input())
    tree = treeeee(V)
    print('#{}'.format(tc), end=' ')
    in_order(1)
    print()