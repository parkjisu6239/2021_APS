import sys
sys.stdin = open('input.txt')

def find_set(x):
    if  x != p[x]:
        return find_set(p[x])
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)



for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    p = list(range(V+1))

    for _ in range(E):
        x, y = map(int, input().split())
        if find_set(x) != find_set(y):
            union(x, y)

    relation = set()
    for i in range(1, V+1):
        relation.add(find_set(i))

    print('#{} {}'.format(tc, len(relation)))
