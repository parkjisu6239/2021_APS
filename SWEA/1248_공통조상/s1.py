import sys
sys.stdin = open('input.txt')

# 1. 트리 구성
def maketree(V, temp):
    tree = [[0, 0, 0] for _ in range(V+1)]

    for i in range(V-1):
        if tree[temp[2*i]][0] == 0:
            tree[temp[2*i]][0] = temp[2*i+1]
        else:
            tree[temp[2 * i]][1] = temp[2 * i + 1]

        tree[temp[2 * i + 1]][2] = temp[2 * i]

    return tree


# 2. 조상 찾기
def findgrandfa(node, i):
    global tree, parent
    if tree[node][2] != 0:
        parent[i].append(tree[node][2])
        findgrandfa(tree[node][2], i)


# 3. 가족 세기
def cnt_family(common_grandfa):
    global cnt
    if common_grandfa:
        cnt += 1
        cnt_family(tree[common_grandfa][0])
        cnt_family(tree[common_grandfa][1])


# 인풋 & 함수 실행
for tc in range(1, int(input())+1):
    V, E, target1, target2 = map(int, input().split())
    temp = list(map(int,input().split()))

    # 1. 트리 구성
    tree = maketree(V, temp)

    # 2. 공통 조상 찾기
    parent = [[], []]
    findgrandfa(target1, 0)
    findgrandfa(target2, 1)

    for i in range(len(parent[1])):
        if parent[1][i] in parent[0]:
            common_grandfa = parent[1][i]
            break

    # 가족 세기
    cnt = 0
    cnt_family(common_grandfa)

    # 출력
    print('#{} {} {}'.format(tc, common_grandfa, cnt))


