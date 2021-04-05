import sys
sys.stdin = open('input.txt')

# 전처리
def treeeee():
    V = int(input())
    # 왼쪽 자식, 오른쪽 자식, 부모, 알파벳
    tree = [[0, 0, 0, ''] for _ in range(V + 1)]

    # 2차원 배열 형태로 정보 넣기
    for _ in range(V):
        # 정점, 알파벳, 왼자식, 오른자식
        info = input().split()

        # 자식 몇명?있는지에 따라 tree에 추가하기
        for i in range(2, len(info)):
            tree[int(info[0])][i-2] = int(info[i])
            tree[int(info[i])][2] = int(info[0])

        # tree의 3번 인덱스 값으로 알파벳 넣기
        tree[int(info[0])][3] = info[1]

    return tree


# 순회
def in_order(node):
    if node:
        in_order(tree[node][0])
        print(tree[node][3], end='')
        in_order(tree[node][1])


# 함수 실행
for tc in range(1, 11):
    tree = treeeee()
    print('#{}'.format(tc), end=' ')
    in_order(1)
    print()