# 조부모가 같으면 사촌

import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def find_cousin(n, k):
    arr = list(map(int, input().split()))
    tree = dict()

    parents = [0] # 부모의 후보, 루트의 부모는 0이라 하자
    p = 0 # 현재 연속된 수의 집합의 부모

    for i in range(n):
        parents.append(arr[i]) # 모든 노드는 부모가 될 수 있다
        if i == 0 or arr[i] > arr[i-1] + 1: # 루트이거나, 연속되지 않으면
            p = parents.pop(0) # 새로운 부모가 필요하다

        if p == 0 or p == arr[0]: # 부모가 0이거나, 부모가 루트인 경우 = 조부모 없음
            tree[arr[i]] = (p, -1)
        else: # 조부모 = 부모의 부모
            tree[arr[i]] = (p, tree[p][0])

    cnt = 0
    for v in arr:
        if tree[v][1] == -1: # 부모가 루트면 사촌 없음
            continue

        if tree[k][0] != tree[v][0] and tree[k][1] == tree[v][1]:
            cnt += 1

    return cnt


while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break

    print(find_cousin(n, k))

