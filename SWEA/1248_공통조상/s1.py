import sys
sys.stdin = open('eval_input.txt')

# 1. 트리 구성
def maketree(V, temp):
    # 트리 초기화 : 정점 + 1개 (인덱스를 맞추기 위해)
    tree = [[0, 0, 0] for _ in range(V+1)]

    # 간선수만큼 반복 : 간선 = 정점 - 1
    for i in range(V-1):
        # 왼쪽, 오른쪽 자식
        if tree[temp[2*i]][0] == 0:
            tree[temp[2*i]][0] = temp[2*i+1]
        else:
            tree[temp[2 * i]][1] = temp[2 * i + 1]
        # 부모
        tree[temp[2 * i + 1]][2] = temp[2 * i]

    return tree


# 2. 조상 찾기
def findgrandfa(node, i):
    global tree, parent
    # 부모가 0 이 아닌 경우
    if tree[node][2] != 0:
        # 부모를 parent에 추가
        parent[i].append(tree[node][2])
        # 부모의 부모를 찾으러 ㄱㄱ
        findgrandfa(tree[node][2], i)


# 3. 가족 세기
def cnt_family(common_grandfa):
    global cnt
    # 공통 조상을 서브트리의 루트로 하여 순회
    # 순회 방법은 상관 X
    if common_grandfa:
        cnt += 1
        cnt_family(tree[common_grandfa][0])
        cnt_family(tree[common_grandfa][1])


# 인풋 & 함수 실행
for tc in range(1, int(input())+1):
    V, E, target1, target2 = map(int, input().split())
    temp = list(map(int,input().split()))
    # print(temp)

    # 1. 트리 구성
    tree = maketree(V, temp)
    # print(tree)


    # 2. 공통 조상 찾기
    parent = [[], []]
    findgrandfa(target1, 0)
    findgrandfa(target2, 1)
    # print(parent)

    for i in range(len(parent[1])):
        if parent[1][i] in parent[0]:
            common_grandfa = parent[1][i]
            break
    # print(common_grandfa)

    # 3. 가족 세기
    cnt = 0
    cnt_family(common_grandfa)
    # print(cnt)

    # 4. 출력
    print('#{} {} {}'.format(tc, common_grandfa, cnt))


